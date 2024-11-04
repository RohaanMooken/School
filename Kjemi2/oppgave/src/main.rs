use plotters::prelude::*;
use std::f64;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Konstanter
    let volum_hcl = 1.0; // Volum i liter
    let konsentrasjon_hcl = 0.1; // mol/L - initial konsentrasjon av HCl
    let mol_naoh_per_tilsetning = 0.01; // Mol av NaOH tilsatt hver gang

    // Initial mol av H+
    let mol_h_plus = konsentrasjon_hcl * volum_hcl;

    // Vektor for å lagre pH-verdier
    let mut ph_verdier: Vec<f64> = Vec::new();

    // Initial pH for 0.1 mol/L HCl
    let initial_ph = -f64::log10(konsentrasjon_hcl);
    ph_verdier.push(initial_ph);
    println!("Tilsetning 0: pH = {}", initial_ph);

    // Beregn pH for hver NaOH-tilsetning
    for i in 1..=21 {
        let total_mol_naoh = i as f64 * mol_naoh_per_tilsetning;
        let ph = if total_mol_naoh < mol_h_plus {
            // Overskudd av HCl gjenstår
            let gjenværende_h_plus_mol = mol_h_plus - total_mol_naoh;
            let konsentrasjon_h_plus = gjenværende_h_plus_mol / volum_hcl;
            -f64::log10(konsentrasjon_h_plus)
        } else {
            // Overskudd av NaOH eller fullstendig nøytralisering
            let overskudd_naoh_mol = total_mol_naoh - mol_h_plus;
            let konsentrasjon_oh_minus = overskudd_naoh_mol / volum_hcl;
            if konsentrasjon_oh_minus > 0.0 {
                14.0 + f64::log10(konsentrasjon_oh_minus)
            } else {
                7.0 // Nøytralt punkt
            }
        };
        ph_verdier.push(ph);
        println!("Tilsetning {}: pH = {}", i, ph);
    }

    // Plotting ved bruk av Plotters crate
    let rot_område = BitMapBackend::new("pH_endringer.png", (640, 480)).into_drawing_area();
    rot_område.fill(&WHITE)?;

    let mut diagram = ChartBuilder::on(&rot_område)
        .caption("endring i pH til HCl ved tilsetning av NaOH", ("sans-serif", 30).into_font())
        .margin(5)
        .x_label_area_size(30)
        .y_label_area_size(30)
        .build_cartesian_2d(0..21, 0f64..16f64)?;

    diagram.configure_mesh().draw()?;

    diagram.draw_series(LineSeries::new(
        (0..=21).map(|x| (x as i32, ph_verdier[x])),
        &BLUE,
    ))?
    .label("pH")
    .legend(|(x, y)| PathElement::new(vec![(x, y), (x + 20, y)], &BLUE));

    diagram.draw_series(PointSeries::of_element(
        (0..=21).map(|x| (x as i32, ph_verdier[x])),
        5,
        &RED,
        &|c, s, st| {
            return EmptyElement::at(c)    // We want to construct a composed element on-the-fly
            + Circle::new((0,0),s,st.filled()); // At this point, the new pixel coordinate is established
        },
    ))?
    .label("pH Points")
    .legend(|(x, y)| Circle::new((x, y), 5, &RED));

    diagram.configure_series_labels()
        .background_style(&WHITE.mix(0.8))
        .border_style(&BLACK)
        .draw()?;

    rot_område.present()?;

    println!("Diagram lagret som 'pH_endringer.png'");
    
    Ok(())
}
