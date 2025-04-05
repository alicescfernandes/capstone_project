import { Badge, DarkThemeToggle } from "flowbite-react";
import { useGetQuarterQuery } from "./api/endpoints";
import { QuarterNavigation } from "./components/QuarterNavigation/QuarterNavigation";
import { Navbar } from "./components/Navbar/Navbar";
import { useState } from "react";

export default function App() {
  const [currentQuarter, setCurrentQuarter] = useState()
  const { data, isLoading, error } = useGetQuarterQuery(currentQuarter);

  return (
    <main>
      <Navbar />
      <QuarterNavigation currentQuarter={currentQuarter} setCurrentQuarter={setCurrentQuarter} />
      <p>{JSON.stringify(data)}</p>
    </main>
  );
}
