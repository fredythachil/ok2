<script>
    // Get references to the Department and Courses dropdowns
    const departmentDropdown = document.getElementById("id_department");
    const courseDropdown = document.getElementById("id_course");

    // Define the courses based on departments
    const coursesByDepartment = {
        commerce: [
            { value: "bba", label: "BBA" },
            { value: "bcom", label: "BCom" },
        ],
        science: [
            { value: "bsc", label: "BSc" },
            { value: "btech", label: "BTech" },
        ],
        arts: [
            { value: "ba", label: "BA" },
            { value: "ma", label: "MA" },
        ],
    };

    // Function to update the Courses dropdown options
    function updateCoursesDropdown() {
        const selectedDepartment = departmentDropdown.value;
        const courses = coursesByDepartment[selectedDepartment] || [];

        // Clear the current options in the Courses dropdown
        courseDropdown.innerHTML = "";

        // Add the default empty option
        const defaultOption = document.createElement("option");
        defaultOption.value = "";
        defaultOption.text = "---------";
        courseDropdown.appendChild(defaultOption);

        // Add options based on the selected department
        courses.forEach((course) => {
            const option = document.createElement("option");
            option.value = course.value;
            option.text = course.label;
            courseDropdown.appendChild(option);
        });
    }

    // Initial update of Courses dropdown based on the selected department
    updateCoursesDropdown();

    // Add an event listener to the Department dropdown to update the Courses dropdown
    departmentDropdown.addEventListener("change", updateCoursesDropdown);
</script>
