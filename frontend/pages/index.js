const Index = () => {
  const today = new Date()

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

  const week = findWeek(findNearMonday(today))

  return (
    <div>
      <h1> Appointment reminder</h1>
      <ul>
        {week.map(day => (
          <li>{JSON.stringify(day)}</li>
        ))}
      </ul>
    </div>
  )
}

export default Index
