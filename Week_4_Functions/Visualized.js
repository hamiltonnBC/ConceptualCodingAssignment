import React, { useState, useEffect } from 'react';
import { Slider } from '@/components/ui/slider';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

const HappinessCalculator = () => {
  const [hoursRelaxing, setHoursRelaxing] = useState(4);
  const [hoursSocializing, setHoursSocializing] = useState(2);
  const [hoursWorking, setHoursWorking] = useState(8);
  const [happinessLevel, setHappinessLevel] = useState(0);

  const calculateHappiness = () => {
    const relaxScore = hoursRelaxing * 2;
    const socialScore = hoursSocializing / 2;
    const workScore = hoursWorking * -2;
    const workLifeBalanceScore = workScore + relaxScore;
    const happiness = Math.floor((relaxScore + socialScore + workLifeBalanceScore) / 3);
    setHappinessLevel(happiness);
  };

  useEffect(() => {
    calculateHappiness();
  }, [hoursRelaxing, hoursSocializing, hoursWorking]);

  const data = [
    { name: 'Relax Score', value: hoursRelaxing * 2 },
    { name: 'Social Score', value: hoursSocializing / 2 },
    { name: 'Work Life Balance', value: (hoursWorking * -2) + (hoursRelaxing * 2) },
  ];

  return (
    <div className="p-4 max-w-3xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Happiness Level Calculator</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Card>
          <CardHeader>
            <CardTitle>Input Values</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div>
                <label className="block mb-2">Hours Relaxing: {hoursRelaxing}</label>
                <Slider
                  value={[hoursRelaxing]}
                  onValueChange={(value) => setHoursRelaxing(value[0])}
                  max={24}
                  step={0.5}
                />
              </div>
              <div>
                <label className="block mb-2">Hours Socializing: {hoursSocializing}</label>
                <Slider
                  value={[hoursSocializing]}
                  onValueChange={(value) => setHoursSocializing(value[0])}
                  max={24}
                  step={0.5}
                />
              </div>
              <div>
                <label className="block mb-2">Hours Working: {hoursWorking}</label>
                <Slider
                  value={[hoursWorking]}
                  onValueChange={(value) => setHoursWorking(value[0])}
                  max={24}
                  step={0.5}
                />
              </div>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>Results</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-center mb-4">
              <h2 className="text-xl font-semibold">Happiness Level</h2>
              <p className="text-4xl font-bold">{happinessLevel}</p>
            </div>
            <ResponsiveContainer width="100%" height={200}>
              <BarChart data={data}>
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="value" fill="#8884d8" />
              </BarChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default HappinessCalculator;