import Signup from "./Signup";
import Login from "./Login";
import MorningCheckin from "./MorningCheckin";
import EveningReflection from "./EveningReflection";
import SkillPractice from "./SkillPractice";

import { Routes, Route, Navigate } from "react-router-dom";

function App() {
  return (
    <Routes>

      {/* default route */}
      <Route path="/" element={<Navigate to="/signup" />} />

      {/* auth pages */}
      <Route path="/signup" element={<Signup />} />
      <Route path="/login" element={<Login />} />

      {/* morning page */}
      <Route path="/morning-checkin" element={<MorningCheckin />} />

      {/* evening page */}
      <Route path="/evening-reflection" element={<EveningReflection />} />

      {/* skill practice page */}
      <Route path="/skill-practice" element={<SkillPractice />} />

    </Routes>
  );
}

export default App;