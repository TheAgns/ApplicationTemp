import { useRouter } from "next/router";

function Map() {
  const router = useRouter();

  return (
    <div>
      {/* <button onClick={handleClick}>View Map</button> */}
      <iframe
        src="/getMap.html"
        style={{ width: "100%", height: "500px", border: "none" }}
      />
    </div>
  );
}

export default Map;
