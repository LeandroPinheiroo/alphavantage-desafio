import React from 'react';
import Chart from "react-google-charts";


export const Dashboard = () => {

    return (
        <div className="col-lg-12" >
            <Chart
    width={'100%'}
    height={'100vh'}
    chartType="AreaChart"
    loader={<div>Loading Chart</div>}
    data={[
      ['Year', 'Sales'],
      ['2013', 1000],
      ['2014', 1170],
      ['2015', 660],
      ['2016', 1030],
    ]}
    options={{
      title: 'Company Performance',
      hAxis: { title: 'Year', titleTextStyle: { color: '#333' } },
      vAxis: { minValue: 0 },
      // For the legend to fit, we make the chart area smaller
      chartArea: { width: '50%', height: '70%' },
      // lineWidth: 25
    }}
  />
        </div>
    );
}
