import React from 'react';
import './../assets/styles/MainContent.css';
import CourseCard from './CourseCard';


const MainContent = () => {
    return (
        <div className="main-content">
            <div className="new-courses">
                <h2>New Courses</h2>
                <div className="course-list">
                    <CourseCard title="Geography" lessons="12 lessons" />
                    <CourseCard title="JavaScript Course" lessons="15 lessons" />
                    <CourseCard title="Photography Course" lessons="8 lessons" />
                </div>
            </div>
            <div className="my-courses">
                <h2>My Courses</h2>
                {/* Repeat course cards */}
            </div>
            <div className="homework-progress">
                <h2>Homework Progress</h2>
                <div className="progress-item">
                    <p>Styling with CSS</p>
                    <span>50%</span>
                </div>
                {/* More progress items */}
            </div>
        </div>
    );
}

export default MainContent;
