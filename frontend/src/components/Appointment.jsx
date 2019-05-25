import React from 'react';

class CreateAppointment extends React.Component {
  constructor() {
    super();
    this.state = {
      providers: [
        {
          pk: '354c8a54-12b5-47ad-af91-235662cc8d71',
          name: 'Diego',
          last_name_1: 'Espinoza',
          last_name_2: 'Salazar',
          known_as: 'Dieguin',
          nro_colegiatura: '12345',
          nro_especialista: '12345',
          specialty: 'traumatologia',
          other_specialty: 'string'
        },
        {
          pk: '05d6fcd6-3d54-4d32-881d-6b12d4862c98',
          name: 'Diana',
          last_name_1: 'Griego',
          last_name_2: 'Miranda',
          known_as: 'Diena Griego',
          nro_colegiatura: '12345',
          nro_especialista: '123456',
          specialty: 'psicologia',
          other_specialty: 'psiquiatria'
        }
      ],
      patients: [
        {
          id: '5cbad076-12ff-4433-a0b1-b7e9e8b2ebb0',
          name: 'Victoria',
          last_name_1: 'Tejeda',
          last_name_2: 'More',
          email: 'Victoria_Tejeda28@yahoo.com',
          phone: '',
          cellphone: '920264914',
          dni: '26384029'
        },
        {
          id: 'e223379b-ccd3-4d11-9999-a8dbaa506a68',
          name: 'Catalina',
          last_name_1: 'Hernadez',
          last_name_2: 'Godoy',
          email: 'Catalina58@gmail.com',
          phone: '',
          cellphone: '921927882',
          dni: '83749875'
        },
        {
          id: 'e838911e-517c-4ff5-ac5d-a31b95d02852',
          name: 'Amalia',
          last_name_1: 'Ocasio',
          last_name_2: 'Barrio',
          email: 'Amalia_Ocasio52@hotmail.com',
          phone: '',
          cellphone: '908876149',
          dni: '27263892'
        }
      ],
      appointment: {}
    };
  }

  handleChange(event) {
    console.log(event.target.value);
  }

  render() {
    const { providers, patients } = this.state;
    return (
      <div>
        <form>
          <label htmlFor="">
            Provide:
            <select name="" id="" onChange={this.handleChange}>
              {providers.map(provider => (
                <option key={provider.pk} value={provider.pk}>
                  {provider.known_as}
                </option>
              ))}
            </select>
          </label>
          <br />
          <label htmlFor="">
            Patien:
            <select name="" id="" onChange={this.handleChange}>
              {patients.map(patient => (
                <option key={patient.id} value={patient.id}>
                  {patient.name}
                </option>
              ))}
            </select>
          </label>
        </form>
      </div>
    );
  }
}

export default CreateAppointment;
