export async function simulateTreaty(countryA: string, countryB: string, objective: string) {
    const res = await fetch("http://localhost:8000/simulate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ country_a: countryA, country_b: countryB, objective }),
    });

    return res.json();
}
