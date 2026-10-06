const API = "";


// -----------------------------
// BMI
// -----------------------------

async function calculateBMI() {

    const weight =
        document.getElementById("weight").value;

    const height =
        document.getElementById("height").value;

    if (!weight || !height) {
        alert("Please enter weight and height");
        return;
    }

    const response = await fetch(
        `${API}/bmi?weight=${weight}&height=${height}`
    );

    const data = await response.json();

    document.getElementById("bmi-result").innerHTML = `

        <div class="result-box">

            <h3>Your BMI: ${data.bmi}</h3>

            <p>
                Category: ${data.category}
            </p>

        </div>

    `;
}


// -----------------------------
// Calories
// -----------------------------

async function calculateCalories() {

    const weight =
        document.getElementById("cal-weight").value;

    const duration =
        document.getElementById("duration").value;

    const activity =
        document.getElementById("activity").value;

    if (!weight || !duration) {
        alert("Please enter all details");
        return;
    }

    const response = await fetch(
        `${API}/calories?weight=${weight}&duration=${duration}&activity=${activity}`
    );

    const data = await response.json();

    document.getElementById("calorie-result").innerHTML = `

        <div class="result-box">

            <h3>🔥 ${data.estimated_calories} Calories</h3>

            <p>
                Activity: ${data.activity}
            </p>

            <p>
                Duration: ${data.duration_minutes} minutes
            </p>

        </div>

    `;
}


// -----------------------------
// Workout
// -----------------------------

async function getWorkout(goal) {

    const response =
        await fetch(`/workout/${goal}`);

    const data =
        await response.json();

    let html = `

        <div class="result-box">

            <h3>💪 ${data.goal.toUpperCase()}</h3>

            <ul>
    `;

    data.workout.forEach(item => {

        html += `<li>${item}</li>`;

    });

    html += `
            </ul>
        </div>
    `;

    document.getElementById(
        "workout-result"
    ).innerHTML = html;

    document
        .getElementById("workout-result")
        .scrollIntoView({
            behavior: "smooth"
        });
}


// -----------------------------
// Diet
// -----------------------------

async function getDiet(goal) {

    const response =
        await fetch(`/diet/${goal}`);

    const data =
        await response.json();

    let html = `

        <div class="result-box">

            <h3>🥗 ${data.goal.toUpperCase()} DIET</h3>

            <ul>
    `;

    data.diet_plan.forEach(item => {

        html += `<li>${item}</li>`;

    });

    html += `
            </ul>
        </div>
    `;

    document.getElementById(
        "diet-result"
    ).innerHTML = html;
}


// -----------------------------
// Exercise Search
// -----------------------------

async function showExercises() {

    const response =
        await fetch("/exercises");

    const data =
        await response.json();

    let html = `

        <div class="result-box">

            <h3>🏋️ Available Exercises</h3>

            <ul>
    `;

    data.forEach(exercise => {

        html += `

            <li>
                <strong>${exercise.name}</strong>
                -
                ${exercise.muscle}
                -
                ${exercise.difficulty}
            </li>

        `;

    });

    html += `
            </ul>
        </div>
    `;

    document.getElementById(
        "workout-result"
    ).innerHTML = html;
}


// -----------------------------
// Scroll helpers
// -----------------------------

function showBMI() {

    document
        .getElementById("bmi-section")
        .scrollIntoView({
            behavior: "smooth"
        });
}


function showCalories() {

    document
        .querySelector(".calculator:nth-of-type(2)")
        .scrollIntoView({
            behavior: "smooth"
        });
}

// -----------------------------
// Personalized Fitness Plan
// -----------------------------

async function createFitnessPlan() {

    const age =
        document.getElementById("plan-age").value;

    const weight =
        document.getElementById("plan-weight").value;

    const height =
        document.getElementById("plan-height").value;

    const goal =
        document.getElementById("plan-goal").value;

    const activity =
        document.getElementById("plan-activity").value;


    if (!age || !weight || !height) {

        alert("Please enter age, weight and height");

        return;
    }


    const url =
        `/fitness-plan?age=${age}&weight=${weight}&height=${height}&goal=${goal}&activity=${activity}`;


    const response = await fetch(url);

    const data = await response.json();


    let workoutHTML = "";

    data.workout.forEach(item => {

        workoutHTML += `<li>${item}</li>`;

    });


    let dietHTML = "";

    data.diet.forEach(item => {

        dietHTML += `<li>${item}</li>`;

    });


    document.getElementById(
        "fitness-plan-result"
    ).innerHTML = `

        <div class="personal-plan">

            <div class="plan-header">

                <p>YOUR PERSONALIZED PLAN</p>

                <h3>${data.goal.toUpperCase()}</h3>

            </div>


            <div class="stats">

                <div>
                    <strong>${data.bmi}</strong>
                    <span>BMI</span>
                </div>

                <div>
                    <strong>${data.category}</strong>
                    <span>CATEGORY</span>
                </div>

                <div>
                    <strong>${data.estimated_daily_calories}</strong>
                    <span>EST. KCAL/DAY</span>
                </div>

            </div>


            <div class="plan-columns">

                <div class="plan-card">

                    <h3>🏋️ WORKOUT</h3>

                    <ul>
                        ${workoutHTML}
                    </ul>

                </div>


                <div class="plan-card">

                    <h3>🥗 DIET</h3>

                    <ul>
                        ${dietHTML}
                    </ul>

                </div>

            </div>

        </div>
    `;


    document
        .getElementById("fitness-plan-result")
        .scrollIntoView({
            behavior: "smooth"
        });
}