import { useState } from "react";
import { useNavigate } from "react-router-dom";

function EveningReflection() {

  const navigate = useNavigate();

  const [form, setForm] = useState({
    win: "",
    lesson: "",
    mistake: "",
    distraction: "",
    mood: 2,
    energy: 2
  });

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  return (
    <div className="flex h-screen bg-gray-100 font-sans">

      {/* Sidebar */}
      <div className="w-64 bg-white shadow-lg p-6 flex flex-col justify-between">

        <div>
          <h1 className="text-blue-600 font-bold text-lg mb-10">
            DAILY GROWTH OS
          </h1>

          <ul className="space-y-6 text-gray-600">

            <li onClick={()=>navigate("/morning-checkin")} className="cursor-pointer">
              Morning Check In
            </li>

            <li className="text-blue-600 cursor-pointer">
              Evening Reflection
            </li>

            <li onClick={()=>navigate("/skill-practice")} className="cursor-pointer">
              Skill Practice
            </li>

          </ul>
        </div>

        <button className="text-blue-500 text-sm">
          Log Out
        </button>

      </div>


      {/* Main Section */}
      <div className="flex-1 p-12">

        <h4 className="text-blue-500 mb-2">
          Observe before ending the day.
        </h4>

        <h1 className="text-3xl font-semibold mb-1">
          Evening Reflection
        </h1>

        <p className="text-gray-500 mb-8">
          Reflect on your day and set intentions for tomorrow
        </p>


        {/* Win */}
        <div className="mb-6">
          <h3 className="font-semibold">Today's Win</h3>

          <input
            name="win"
            value={form.win}
            onChange={handleChange}
            className="w-[500px] p-3 bg-gray-200 rounded-lg shadow"
          />
        </div>


        {/* Lesson */}
        <div className="mb-6">
          <h3 className="font-semibold">Lesson Learned</h3>

          <input
            name="lesson"
            value={form.lesson}
            onChange={handleChange}
            className="w-[500px] p-3 bg-gray-200 rounded-lg shadow"
          />
        </div>


        {/* Mistake */}
        <div className="mb-6">
          <h3 className="font-semibold">Today's Mistake</h3>

          <input
            name="mistake"
            value={form.mistake}
            onChange={handleChange}
            className="w-[500px] p-3 bg-gray-200 rounded-lg shadow"
          />
        </div>


        {/* Distraction */}
        <div className="mb-8">
          <h3 className="font-semibold">Primary Source of Distraction</h3>

          <input
            name="distraction"
            value={form.distraction}
            onChange={handleChange}
            className="w-[500px] p-3 bg-gray-200 rounded-lg shadow"
          />
        </div>


        {/* Mood */}
        <div className="mb-6">
          <h3 className="font-semibold mb-2">Mood Rating</h3>

          <input
            type="range"
            min="1"
            max="5"
            value={form.mood}
            onChange={(e)=>setForm({...form,mood:e.target.value})}
            className="w-96"
          />

          <span className="ml-3">{form.mood}</span>
        </div>


        {/* Energy */}
        <div className="mb-8">
          <h3 className="font-semibold mb-2">Energy Levels</h3>

          <input
            type="range"
            min="1"
            max="5"
            value={form.energy}
            onChange={(e)=>setForm({...form,energy:e.target.value})}
            className="w-96"
          />

          <span className="ml-3">{form.energy}</span>
        </div>


        <button className="bg-gray-700 text-white px-12 py-3 rounded-lg shadow">
          Save and Continue
        </button>

      </div>
    </div>
  );
}

export default EveningReflection;