import { useState } from "react";
import { simulateTreaty } from "../services/api";

export default function SimulationPage() {
    const [log, setLog] = useState<string[]>([]);
    const [a, setA] = useState("USA");
    const [b, setB] = useState("China");
    const [objective, setObjective] = useState("Climate Treaty");

    const runSim = async () => {
        const result = await simulateTreaty(a, b, objective);
        setLog([
            `???? ${result.a_message}`,
            `???? ${result.b_message}`,
            `?? ${result.next_step}`,
        ]);
    };

    return (
        <div className="p-6">
            <h1 className="text-2xl font-bold mb-4">Diplomatic Simulation</h1>
            <div className="mb-2">
                <select onChange={e => setA(e.target.value)} value={a}>
                    <option>USA</option><option>Russia</option><option>India</option>
                </select>
                <select onChange={e => setB(e.target.value)} value={b}>
                    <option>China</option><option>EU</option><option>Brazil</option>
                </select>
                <input
                    value={objective}
                    onChange={e => setObjective(e.target.value)}
                    placeholder="Objective"
                    className="ml-2 border p-1"
                />
                <button onClick={runSim} className="ml-2 px-4 py-1 bg-blue-500 text-white">Simulate</button>
            </div>
            <div className="mt-4 space-y-2">
                {log.map((line, i) => <p key={i}>{line}</p>)}
            </div>
        </div>
    );
}
