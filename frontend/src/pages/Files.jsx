import { useEffect, useState } from "react";
import api from "../services/api";

function Files() {
  const [files, setFiles] = useState([]);

  useEffect(() => {
    api.get("/files").then((res) => setFiles(res.data));
  }, []);

  return (
    <div>
      <h2>Your Files</h2>
      <ul>
        {files.map((f) => (
          <li key={f.id}>{f.filename}</li>
        ))}
      </ul>
    </div>
  );
}

export default Files;

