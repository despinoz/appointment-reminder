import React from 'react';

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      today: new Date(),
      monday: new Date(),
      spanishWeekDays: ['dom', 'lun', 'mar', 'mie', 'jue', 'vie', 'sab'],
      citas: [],
      currentWeek: []
    };
  }

  componentDidMount() {
    this.findNearMonday(this.state.today);
  }

  findNearMonday(date) {
    const monday = new Date();
    const difference = date.getDay() === 0 ? 6 : date.getDay() - 1;
    monday.setDate(date.getDate() - difference);
    this.setState({
      monday
    });
    this.findWeek(monday);
  }

  findWeek(monday) {
    let actualDate = new Date();
    let currentWeek = [];
    for (let i = 0; i < 7; i++) {
      actualDate.setDate(monday.getDate() + i);
      currentWeek[i] = new Date(actualDate);
    }
    this.setState({
      currentWeek
    });
  }

  prevWeek(monday) {
    const prevMonday = new Date();
    prevMonday.setDate(monday.getDate() - 7);
    this.setState({
      monday: prevMonday
    });
    this.findWeek(prevMonday);
  }

  nextWeek(monday) {
    const nextMonday = new Date();
    nextMonday.setDate(monday.getDate() + 7);
    this.setState({
      monday: nextMonday
    });
    this.findWeek(nextMonday);
  }

  render() {
    const { currentWeek } = this.state;
    return (
      <div>
        <header>
          <h1>Recordatorio de Citas</h1>
        </header>
        <hr />
        <h2>Citas</h2>
        <button onClick={() => this.prevWeek(this.state.monday)}>prev</button>
        <div>CURRET WEEK</div>
        <button onClick={() => this.nextWeek(this.state.monday)}>next</button>
        <div>
          {currentWeek.map(day => (
            <div key={day}>
              <div>
                {this.state.spanishWeekDays[day.getDay()] + ' ' + day.getDate()}
              </div>
              <button>crear cita</button>
            </div>
          ))}
        </div>
      </div>
    );
  }
}

export default App;
