import { useState } from "react";
import { Link } from "react-router-dom";

function Signup() {
  // this is input state
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    confirm_password: ""});
  //this is Error state
  const [errors, setErrors] = useState({});

  //Handle input change
  const handleChange = (e) => {
    setFormData({
      ...formData,[e.target.name]: e.target.value});
    //Removing error while typing
    setErrors({
      ...errors,[e.target.name]: ""}); 
    };


  // stops page from reloding and handle form submisiion and collect error
  const handleSubmit = async (e) => {
    e.preventDefault();
    let newErrors = {};
    
    
    // Frontend validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.com$/;
    if (!emailRegex.test(formData.email)) {
      newErrors.email = "Enter a valid email address"; }
    if (!formData.email) {
      newErrors.email = "Email is required"; }
    if (formData.password !== formData.confirm_password) 
      {
      newErrors.confirm_password = "Passwords do not match"; }



    // If any frontend error exists stop here
    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return
    }

    // here fecthig backend api
      try{
    const response = await fetch("http://127.0.0.1:8000/auth/signup",
    {method:"POST",
      headers:{"Content-Type": "application/json"},body:JSON.stringify(formData)});
      const data = await response.json();
     
      if (response.ok){
        setErrors({});alert("singup done");
      }else{
        setErrors({email:data.detail});}}
        catch (error){console.error("Error",error);}};
    
        
        // here now for html part
  return (
  <div className="flex h-screen font-sans">
    {/* Left section of text and input */}
    <div className="w-1/2 flex justify-center items-center bg-white">
      <div className="w-3/5">
        <h2 className="text-[28px] mb-1">
          Get Started Now!
        </h2>
        <p className="text-gray-500 mb-8">
          Track habits, skills and reflection.
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



          <label className="block text-sm mb-1">
            Confirm Password
          </label>
          <input
            type="password"
            name="confirm_password"
            value={formData.confirm_password}
            onChange={handleChange}
            placeholder="Confirm your password"
            className="w-full p-3 mb-5 rounded-lg bg-gray-200 shadow-md outline-none"
          />
          {errors.confirm_password && (
            <p className="text-red-500 text-xs -mt-3 mb-4">
              {errors.confirm_password}
            </p>
          )}

          <button
            type="submit"
            className="ml-36 w-2/5 p-3 bg-green-700 text-white rounded-lg text-base cursor-pointer transition duration-300 hover:bg-black"
          >
            Sign Up
          </button>

        </form>

        <p className="mt-4 text-sm ml-40">
          Have an account?{" "}
          <Link to="/login" className="text-blue-600 cursor-pointer">
            Sign In
          </Link>
        </p>
      </div>
    </div>

    {/* Right section bg image */}
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

export default Signup;