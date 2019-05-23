const Index = () => {
  const today = new Date()
  const spanishWeekDays = ['dom', 'lun', 'mar', 'mie', 'jue', 'vie', 'sab']

  const findNearMonday = function(date) {
    const monday = new Date()
    const difference = date.getDay() === 0 ? 6 : date.getDay() - 1
    monday.setDate(date.getDate() - difference)
    return monday
  }

  const findWeek = function(monday) {
    let actualDate = new Date()
    let week = []
    for (let i = 0; i < 7; i++) {
      actualDate.setDate(monday.getDate() + i)
      week[i] = new Date(actualDate)
    }
    return week
  }

  // const monday = findNearMonday(today)
  const week = findWeek(findNearMonday(today))

  const prevWeek = function(monday) {
    const prevMonday = new Date()
    prevMonday.setDate(date.getDate() - 7)
  }

  return (
    <div>
      <h1> Appointment reminder</h1>
      <button onClick={() => console.log('hi')}>prev week</button>
      <div>{JSON.stringify(week[0].getDate())}</div>
      <button>next week</button>
      <div>
        {week.map(day => (
          <div key={day}>
            <div>{spanishWeekDays[day.getDay()] + ' ' + day.getDate()}</div>
            {/* <button>añadir cita</button> */}
          </div>
        ))}
      </div>
    </div>
  )
}

export default Index
