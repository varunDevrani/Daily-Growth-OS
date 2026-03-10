import { useState } from "react";
import { useNavigate } from "react-router-dom";

function SkillPractice(){

  const navigate = useNavigate();

  const [skills,setSkills] = useState([
    {
      id:1,
      name:"Python",
      activities:[
        {
          id:1,
          text:"Create a list of 5 numbers and print their sum",
          done:false,
          priority:false,
          protect:false
        }
      ]
    }
  ]);

  const [newSkill,setNewSkill] = useState("");
  const [newActivity,setNewActivity] = useState({});

  const addSkill = () => {

    if(!newSkill.trim()) return;

    setSkills([
      ...skills,
      { id:Date.now(), name:newSkill, activities:[] }
    ]);

    setNewSkill("");
  };

  const deleteSkill = (id) => {
    setSkills(skills.filter(s => s.id !== id));
  };

  const toggleDone = (skillId,actId) => {

    setSkills(skills.map(s =>
      s.id === skillId
      ? {
        ...s,
        activities:s.activities.map(a =>
          a.id === actId ? {...a,done:!a.done} : a
        )
      }
      : s
    ));
  };

  const togglePriority = (skillId,actId) => {

    setSkills(skills.map(s =>
      s.id === skillId
      ? {
        ...s,
        activities:s.activities.map(a =>
          a.id === actId ? {...a,priority:!a.priority} : a
        )
      }
      : s
    ));
  };

  const toggleProtect = (skillId,actId) => {

    setSkills(skills.map(s =>
      s.id === skillId
      ? {
        ...s,
        activities:s.activities.map(a =>
          a.id === actId ? {...a,protect:!a.protect} : a
        )
      }
      : s
    ));
  };

  const deleteActivity = (skillId,actId) => {

    setSkills(skills.map(s =>
      s.id === skillId
      ? {...s,activities:s.activities.filter(a=>a.id!==actId)}
      : s
    ));
  };

  const addActivity = (skillId) => {

    const text = newActivity[skillId];

    if(!text?.trim()) return;

    const activity = {
      id:Date.now(),
      text,
      done:false,
      priority:false,
      protect:false
    };

    setSkills(skills.map(s =>
      s.id === skillId
      ? {...s,activities:[...s.activities,activity]}
      : s
    ));

    setNewActivity({...newActivity,[skillId]:""});
  };

  return(

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

            <li onClick={()=>navigate("/evening-reflection")} className="cursor-pointer">
              Evening Reflection
            </li>

            <li className="text-blue-600 cursor-pointer">
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

        <h4 className="text-blue-500 mb-2">
          Skills worked on today
        </h4>

        <h1 className="text-3xl font-semibold mb-6">
          Skill Practice
        </h1>

        {/* Add Skill */}
        <div className="flex gap-3 mb-10">

          <input
            value={newSkill}
            onChange={(e)=>setNewSkill(e.target.value)}
            placeholder="New skill..."
            className="bg-gray-200 px-3 py-2 rounded w-64"
          />

          <button
            onClick={addSkill}
            className="bg-blue-500 text-white px-4 py-2 rounded shadow"
          >
            + Add Skill
          </button>

        </div>


        {skills.map(skill => (

          <div key={skill.id} className="mb-10">

            <div className="flex justify-between mb-4">

              <h2 className="text-xl font-semibold">
                {skill.name}
              </h2>

              <button
                onClick={()=>deleteSkill(skill.id)}
                className="bg-red-400 text-white px-3 py-1 rounded"
              >
                Delete
              </button>

            </div>


            {skill.activities.map(a => (

              <div
                key={a.id}
                className="flex justify-between items-center bg-white shadow rounded-lg px-4 py-3 mb-3 w-[520px] transition hover:shadow-lg"
              >

                <div className="flex items-center gap-3">

                  <input
                    type="checkbox"
                    checked={a.done}
                    onChange={()=>toggleDone(skill.id,a.id)}
                  />

                  <p className={`${a.done ? "line-through text-gray-400" : ""}`}>
                    {a.text}
                  </p>

                </div>

                <div className="flex gap-4 text-xl">

                  <button
                    onClick={()=>togglePriority(skill.id,a.id)}
                    className={`transition transform hover:scale-125
                    ${a.priority
                      ? "text-yellow-400 drop-shadow-[0_0_6px_gold]"
                      : "text-gray-400 hover:text-yellow-400"}
                    `}
                  >
                    ⭐
                  </button>

                  <button
                    onClick={()=>toggleProtect(skill.id,a.id)}
                    className={`transition transform hover:scale-125
                    ${a.protect
                      ? "text-blue-500 drop-shadow-[0_0_6px_lightblue]"
                      : "text-gray-400 hover:text-blue-500"}
                    `}
                  >
                    {a.protect ? "🔒" : "🔓"}
                  </button>

                  <button
                    onClick={()=>deleteActivity(skill.id,a.id)}
                    className="text-red-400 hover:scale-125 transition"
                  >
                    🗑
                  </button>

                </div>

              </div>

            ))}

            <div className="flex gap-3">

              <input
                value={newActivity[skill.id] || ""}
                onChange={(e)=>setNewActivity({...newActivity,[skill.id]:e.target.value})}
                placeholder="New activity..."
                className="bg-gray-200 px-3 py-2 rounded w-64"
              />

              <button
                onClick={()=>addActivity(skill.id)}
                className="bg-blue-500 text-white px-4 py-2 rounded shadow"
              >
                + Add Activity
              </button>

            </div>

          </div>

        ))}

      </div>
    </div>
  );
}

export default SkillPractice;