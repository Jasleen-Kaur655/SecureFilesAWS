// pages/Login.jsx
import { useState } from "react";
import api from "../services/api";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [msg, setMsg] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    setMsg("");

    if (!email || !password) {
      setMsg("Please enter both email and password");
      return;
    }

    try {
      const response = await api.post("/login", { email, password });
      if (response.data.success) {
        setMsg("Login successful ✅");
        // You can redirect the user here
      } else {
        setMsg(response.data.message || "Login failed ❌");
      }
    } catch (err) {
      setMsg("Server error. Please try again later.");
      console.error(err);
    }
  };

  return (
    <div style={{ maxWidth: "400px", margin: "50px auto" }}>
      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <div>
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div style={{ marginTop: "10px" }}>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit" style={{ marginTop: "15px" }}>
          Login
        </button>
      </form>
      {msg && <p style={{ marginTop: "15px" }}>{msg}</p>}
    </div>
  );
}

export default Login;
