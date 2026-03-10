import { useState } from "react";
import { useNavigate } from "react-router-dom";

function MorningCheckin() {

  const navigate = useNavigate();

  const [confidence, setConfidence] = useState(2);

  const [activities, setActivities] = useState([
    {
      id: 1,
      text: "drink more than 500ml of water",
      done: false,
      priority: false,
      protect: false
    },
    {
      id: 2,
      text: "take a 20 min walk",
      done: false,
      priority: false,
      protect: false
    }
  ]);

  const [newActivity, setNewActivity] = useState("");

  const toggleDone = (id) => {
    setActivities(
      activities.map((a) =>
        a.id === id ? { ...a, done: !a.done } : a
      )
    );
  };

  const togglePriority = (id) => {
    setActivities(
      activities.map((a) =>
        a.id === id ? { ...a, priority: !a.priority } : a
      )
    );
  };

  const toggleProtect = (id) => {
    setActivities(
      activities.map((a) =>
        a.id === id ? { ...a, protect: !a.protect } : a
      )
    );
  };

  const deleteActivity = (id) => {
    setActivities(activities.filter((a) => a.id !== id));
  };

  const addActivity = () => {
    if (!newActivity.trim()) return;

    const newItem = {
      id: Date.now(),
      text: newActivity,
      done: false,
      priority: false,
      protect: false
    };

    setActivities([...activities, newItem]);
    setNewActivity("");
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

            <li onClick={()=>navigate("/morning-checkin")} className="text-blue-600 cursor-pointer">
              Morning Check In
            </li>

            <li onClick={()=>navigate("/evening-reflection")} className="cursor-pointer">
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

      {/* Main */}
      <div className="flex-1 p-12">

        <h4 className="text-blue-500 mb-2">What matters today?</h4>

        <h1 className="text-3xl font-semibold mb-1">
          Morning Check In
        </h1>

        <p className="text-gray-500 mb-8">
          Set your intentions for today.
        </p>

        {/* Confidence */}
        <div className="mb-10">

          <h3 className="font-semibold mb-2">
            Confidence Rating
          </h3>

          <input
            type="range"
            min="1"
            max="5"
            value={confidence}
            onChange={(e) => setConfidence(e.target.value)}
            className="w-96"
          />

          <span className="ml-3">{confidence}</span>

        </div>

        {/* Activities */}
        <div className="mb-8">

          <h3 className="font-semibold mb-4">
            Morning Activities
          </h3>

          {activities.map((a) => (

            <div
              key={a.id}
              className="flex items-center justify-between bg-white shadow rounded-lg px-4 py-3 mb-4 w-[520px] transition hover:shadow-lg"
            >

              <div className="flex items-center gap-3">

                <input
                  type="checkbox"
                  checked={a.done}
                  onChange={() => toggleDone(a.id)}
                />

                <p className={`${a.done ? "line-through text-gray-400" : ""}`}>
                  {a.text}
                </p>

              </div>

              <div className="flex gap-4 text-xl">

                {/* Priority */}
                <button
                  onClick={() => togglePriority(a.id)}
                  className={`transition transform hover:scale-125
                  ${a.priority
                    ? "text-yellow-400 drop-shadow-[0_0_6px_gold]"
                    : "text-gray-400 hover:text-yellow-400"}
                  `}
                >
                  ⭐
                </button>

                {/* Protect */}
                <button
                  onClick={() => toggleProtect(a.id)}
                  className={`transition transform hover:scale-125
                  ${a.protect
                    ? "text-blue-500 drop-shadow-[0_0_6px_lightblue]"
                    : "text-gray-400 hover:text-blue-500"}
                  `}
                >
                  {a.protect ? "🔒" : "🔓"}
                </button>

                {/* Delete */}
                <button
                  onClick={() => deleteActivity(a.id)}
                  className="text-red-400 hover:scale-125 transition"
                >
                  🗑
                </button>

              </div>

            </div>
          ))}

          {/* Add Activity */}
          <div className="flex gap-3 mt-4">

            <input
              type="text"
              value={newActivity}
              onChange={(e) => setNewActivity(e.target.value)}
              placeholder="New activity..."
              className="bg-gray-200 px-3 py-2 rounded w-64"
            />

            <button
              onClick={addActivity}
              className="bg-blue-500 text-white px-4 py-2 rounded shadow hover:shadow-lg"
            >
              + Add Activity
            </button>

          </div>

        </div>

        <button className="bg-gray-700 text-white px-12 py-3 rounded-lg shadow">
          Save and Continue
        </button>

      </div>
    </div>
  );
}

export default MorningCheckin;