import React from 'react';
import './../assets/styles/CourseCard.css';

const CourseCard = ({ title, lessons }) => {
    return (
        <div className="course-card">
            <h3>{title}</h3>
            <p>{lessons}</p>
        </div>
    );
}

export default CourseCard;
