import { useState } from "react";
import { Link } from "react-router-dom";

function Login() {

  // input state
  const [formData, setFormData] = useState({
    email: "",
    password: ""
  });

  // error state
  const [errors, setErrors] = useState({});

  // handle input change
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });

    // remove error while typing
    setErrors({
      ...errors,
      [e.target.name]: ""
    });
  };

  // handle form submit
  const handleSubmit = async (e) => {
    e.preventDefault();

    let newErrors = {};

    // frontend validation
    if (!formData.email) {
      newErrors.email = "Email is required";
    }

    if (!formData.password) {
      newErrors.password = "Password is required";
    }

    // stop if validation error
    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
      });

      const data = await response.json();

      if (response.ok) {
        alert("Login successful");

        // if backend returns token
        if (data.access_token) {
          localStorage.setItem("token", data.access_token);
        }

      } else {
        setErrors({ email: data.detail });
      }

    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="flex h-screen font-sans">

      {/* Left Section */}
      <div className="w-1/2 flex justify-center items-center bg-white">
        <div className="w-3/5">

          <h2 className="text-[28px] mb-1">
            Welcome Back!
          </h2>

          <p className="text-gray-500 mb-8">
            Login to continue your journey.
          </p>

          <form onSubmit={handleSubmit}>

            <label className="block text-sm mb-1">
              Email address
            </label>

            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="Enter your email"
              className="w-full p-3 mb-5 rounded-lg bg-gray-200 shadow-md outline-none"
            />

            {errors.email && (
              <p className="text-red-500 text-xs -mt-3 mb-4">
                {errors.email}
              </p>
            )}

            <label className="block text-sm mb-1">
              Password
            </label>

            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              placeholder="Enter your password"
              className="w-full p-3 mb-5 rounded-lg bg-gray-200 shadow-md outline-none"
            />

            {errors.password && (
              <p className="text-red-500 text-xs -mt-3 mb-4">
                {errors.password}
              </p>
            )}

            <button
              type="submit"
              className="ml-36 w-2/5 p-3 bg-green-700 text-white rounded-lg text-base cursor-pointer transition duration-300 hover:bg-black"
            >
              Login
            </button>

          </form>

          <p className="mt-4 text-sm ml-36">
            Don't have an account?{" "}
            <Link to="/signup" className="text-blue-600 cursor-pointer">
              Sign Up
            </Link>
          </p>

        </div>
      </div>

      {/* Right Section */}
      <div
        className="w-1/2 bg-cover bg-center bg-no-repeat rounded-[6%]"
        style={{
          backgroundImage:
            "url('https://miro.medium.com/v2/resize:fit:1100/format:webp/0*KztCa4T9Mx6O-UU7')",
        }}
      ></div>

    </div>
  );
}

export default Login;