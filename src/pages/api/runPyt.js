import { spawn } from "child_process";

export default async function handler(req, res) {
  // Run the Python script using the `spawn` function
  const process = spawn("streamlit", [
    "run",
    "/Users/markusagnsgaard/Desktop/App/nextapp/public/map.py",
  ]);

  // Log any errors that occur
  process.on("error", (err) => {
    console.error(err);
    res.status(500).end();
  });

  // Send a response when the Python script finishes running
  process.on("exit", (code) => {
    res.status(200).json({ message: "Python script finished running!" });
  });
}
