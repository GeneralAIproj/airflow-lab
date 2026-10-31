Q. 1 — Identify the Airflow Responsibility
Match each requirement to the main Airflow component or concept.

A. Decide which task instance is ready to run.
B. Show DAG and task status to a user.
C. Keep run history and task-state information.
D. Launch ready tasks according to the configured execution method.


A -> Scheduler
B -> Webserver / UI
C -> Metadata database
D -> Executor


Q. 3 — Draw the Airflow Component Flow
Draw a simple flow using:

DAG file
Scheduler
Metadata database
Executor
Task
Webserver / UI


flowchart LR
    A["DAG File"] --> B["Scheduler"]
    B --> C["Metadata Database"]
    B --> D["Executor"]
    D --> E["Task"]
    C --> F["Webserver / UI"]



Q. 4 — MCQ: Scheduler
Which component mainly decides which task instances are ready to run?

B. Scheduler

Q. 5 -- Explain what schedule=None means 

schedule=None means the DAG does not create normal scheduled runs. It can still be triggered manually.

Q. 6 — Read a Task State Scenario
A DAG run contains:

extract_orders = success
clean_orders = failed
build_report = upstream_failed

extract_orders completed successfully.

clean_orders failed.

build_report did not run successfully because the task it depended on failed.

Q. 7 — Create Three Independent Tasks
Create a complete DAG with:

extract
clean
report

Copy

Explain
Dependencies:

extract -> clean -> report

Q. 9 — DAG or Task?
Classify each description.

A. The complete workflow definition.
B. One unit of work inside the workflow.
C. A specific run of one task for one DAG run.

Copy

Explain
Choose from:

DAG
Task
Task instance

Answer: 
A -> DAG
B -> Task
C -> Task instance


Q. 11 — Explain Scheduler vs Executor
Responsibility	Component
Decides what is ready	Scheduler
Controls how ready tasks are launched	Executor
Looks at task dependencies	Scheduler
Runs using the configured execution method	Executor


Q. 12 — MCQ: Task Instance

A. One actual run of a task for a particular DAG run


Part 4 — Operators, DAG Structure, and Dependencies
Q. 13 — Identify the Operator
Look at:

from airflow.operators.bash import BashOperator

Copy

Explain
What is the purpose of BashOperator in a DAG?


Answer: 

BashOperator is an operator used to create a task that runs a Bash command.

The operator is the task template. The task created from it is one unit of work in the DAG.

Q. 15 — Fix a Dependency Mistake
The intended order is:

extract -> transform -> validate

Copy

Explain
But this DAG uses:

validate >> transform >> extract

Copy

Explain
Write a complete corrected DAG.


Q. 16 — MCQ: Operator
Which statement is correct?

A. An operator replaces the scheduler. B. An operator is the metadata database. C. An operator is always the same as a DAG run. D. An operator is a task template used to create a task.

Answer: D
