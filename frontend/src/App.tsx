import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import SimulationPage from "./pages/Simulation";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<SimulationPage />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;