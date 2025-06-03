import React from "react";
import { useState } from "react";
import axios from "axios";

type SimulationResult = {
    a_message: string;
    b_message: string;
    next_step: string;
};

export default function SimulationPage() {
    const [a, setA] = useState("USA");
    const [b, setB] = useState("China");
    const [objective, setObjective] = useState("Trade Agreement");
    const [result, setResult] = useState<SimulationResult | null>(null);

    async function simulateTurn() {
        try {
            const res = await axios.post("http://localhost:8000/simulate", {
                country_a: a,
                country_b: b,
                objective: objective
            });
            setResult(res.data);
        } catch (error) {
            setResult({
                a_message: "Error",
                b_message: "Could not fetch simulation result.",
                next_step: ""
            });
        }
    }

    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold mb-4">Treaty Negotiation Simulator</h1>

            <div className="space-y-2">
                <div>
                    <label>Country A:</label>
                    <select value={a} onChange={(e) => setA(e.target.value)}>
                        <option>USA</option><option>China</option><option>Russia</option><option>EU</option>
                    </select>
                </div>

                <div>
                    <label>Country B:</label>
                    <select value={b} onChange={(e) => setB(e.target.value)}>
                        <option>USA</option><option>China</option><option>Russia</option><option>EU</option>
                    </select>
                </div>

                <div>
                    <label>Objective:</label>
                    <input type="text" value={objective} onChange={(e) => setObjective(e.target.value)} />
                </div>

                <button onClick={simulateTurn} className="bg-blue-500 text-white px-4 py-2 rounded">Simulate Turn</button>
            </div>

            {result && (
                <div className="mt-6 bg-gray-100 p-4 rounded">
                    <p><strong>{a}:</strong> {result.a_message}</p>
                    <p><strong>{b}:</strong> {result.b_message}</p>
                    <p className="italic">{result.next_step}</p>
                </div>
            )}
        </div>
    );
}
