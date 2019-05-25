import React from 'react';
import CreateAppointment from './Appointment';

class Day extends React.Component {
  constructor() {
    super();
    this.state = {
      crearCita: false
    };
    this.crearCita = this.crearCita.bind(this);
  }

  crearCita() {
    this.setState({ crearCita: true });
  }

  render() {
    return (
      <div>
        <div>
          {this.props.spanishWeekDays[this.props.day.getDay()] +
            ' ' +
            this.props.day.getDate()}
        </div>
        <button onClick={this.crearCita}>crear cita</button>
        {this.state.crearCita && <CreateAppointment />}
      </div>
    );
  }
}

export default Day;
