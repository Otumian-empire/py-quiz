-- source for questions 
-- https://sheir.org/edu/
-- https://examradar.com/
-- https://www.examveda.com/
-- https://byjus.com/
-- 
BEGIN TRANSACTION;

INSERT INTO
    "category" (name)
VALUES
    ("MATHEMATICS"),
    ("COMPUTER SCIENCE"),
    ("BUSINESS"),
    ("ENGLISH"),
    ("BIOLOGY");

INSERT INTO
    "quiz" ("cat_id", "question", "options", "answer")
VALUES
    (
        (
            SELECT
                id
            FROM
                "category"
            WHERE
                name = "MATHEMATICS"
        ),
        "Which of the following triangles have the same side lengths?",
        "Scalene, Isosceles, Equilateral, None",
        "Equilateral"
    ),
    (
        (
            SELECT
                id
            FROM
                "category"
            WHERE
                name = "MATHEMATICS"
        ),
        "D and E are the midpoints of side AB and AC of a triangle ABC, respectively and BC=6cm. If DE || BC, then the length of DE is?",
        "2.5, 3, 5, 6",
        "3"
    ),
    (
        (
            SELECT
                id
            FROM
                "category"
            WHERE
                name = "MATHEMATICS"
        ),
        "If perimeter of a triangle is 100cm and the length of two sides are 30cm and 40cm, the length of third side will be?",
        "30cm, 40cm, 50cm, 60cm",
        "30cm"
    ),
    (
        (
            SELECT
                id
            FROM
                "category"
            WHERE
                name = "COMPUTER SCIENCE"
        ),
        "ALU stands for?",
        "Arithmetic Logic Unit, Application Logic Unit, Array Logic Unit, None",
        "Arithmetic Logic Unit"
    ),
    (
        (
            SELECT
                id
            FROM
                "category"
            WHERE
                name = "COMPUTER SCIENCE"
        ),
        "The major language of World Wide Web (WWW) is?",
        "PHP, HTML, PYTHON, Web Browser",
        "HTML"
    ),
    (
        (
            SELECT
                id
            FROM
                "category"
            WHERE
                name = "COMPUTER SCIENCE"
        ),
        "Bundling data and functions together is known as?",
        "debugging, encapsulation, overloading, polymorphism",
        "encapsulation"
    ),
    (
        (
            SELECT
                id
            FROM
                "category"
            WHERE
                name = "BUSINESS"
        ),
        "Which of the following is part of the double entry system in Accounting?",
        "Cash book, General journal, Sales journal, Trial balance",
        "Cash book"
    ),
    (
        (
            SELECT
                id
            FROM
                "category"
            WHERE
                name = "BUSINESS"
        ),
        "The correct form of Accounting equation is?",
        "Assets + Liabilities=Equity, Assets – Liabilities=Equity, Assets – Receivable=Equity, Assets + Receivable=Equity",
        "Assets – Liabilities=Equity"
    ),
    (
        (
            SELECT
                id
            FROM
                "category"
            WHERE
                name = "BUSINESS"
        ),
        "The fundamental concept of Economics about resources is that the resources are?",
        "equally distributed, unequally distributed, scarce, unlimited",
        "scarce"
    ),
    (
        (
            SELECT
                id
            FROM
                "category"
            WHERE
                name = "ENGLISH"
        ),
        "She can’t run anymore, she is _____ tired.",
        "too, so, such, so such",
        "too"
    ),
    (
        (
            SELECT
                id
            FROM
                "category"
            WHERE
                name = "ENGLISH"
        ),
        "While UK has earned record revenue this year, __________ well behind in exports.",
        "it still lag, it still lags, it lag still, it lags still",
        "it still lags"
    ),
    (
        (
            SELECT
                id
            FROM
                "category"
            WHERE
                name = "ENGLISH"
        ),
        "If I have money, I __________ it tomorrow.",
        "will purchase, would purchase, have purchase, have purchased",
        "will purchase"
    ),
    (
        (
            SELECT
                id
            FROM
                "category"
            WHERE
                name = "BIOLOGY"
        ),
        "What is essential for the formation of hemoglobin?",
        "Calcium, Iron, Water, Carbohydrates",
        "Iron"
    ),
    (
        (
            SELECT
                id
            FROM
                "category"
            WHERE
                name = "BIOLOGY"
        ),
        "The average internal temperature of human body is?",
        "35 °C, 36 °C, 37 °C, 38 °C",
        "37 °C"
    ),
    (
        (
            SELECT
                id
            FROM
                "category"
            WHERE
                name = "BIOLOGY"
        ),
        "Severe deficiency of Vitamin-D results in?",
        "scurvy, rickets, night blindness, osteomalacia",
        "rickets"
    );

COMMIT;