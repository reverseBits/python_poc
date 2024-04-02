**Step to run the project (celery and flower)**
 1. Change the path using
      - **cd celery_with_django**
 2. Activate the environment using
      - **& D:\ReverseBits\Projects\django\celery_with_django\env\Scripts\activate.ps1**

   - Follow above two step to each terminal.
 3. Run the python using
      - **python manage.py runserver**
 4. Run celery worker using 
      - **celery -A django_celery_project.celery worker -n worker_for_add_sub -Q add-queue,sub-queue -l INFO -P gevent**
      - **celery -A django_celery_project.celery worker -n worker_for_send_mail -Q sendmail -l INFO -P gevent**
 5. Run flower using 
      - **celery --broker=redis://localhost:6379// flower**



**Flow of celery and redis in django**
   1. Task Enqueuing:
      - When a user triggers an action in the Django application, such as submitting a form or accessing a particular URL, a corresponding view function is called.
      - Inside the view function, Celery tasks are enqueued using the delay method. For example, the add and sub tasks are enqueued in the test view, while the send_mail_func task is enqueued in the send_mail_to_all view.
      <br>
   2. Message Queue (Redis):
       -  The enqueued tasks are sent to Redis, which acts as a message broker. Each task is placed in a specific queue (channel) based on its configuration or routing rules.
       <br>

   3. Celery Workers:
       - Celery workers continuously monitor the Redis message queues for new tasks.
       - When a worker detects a new task in the queue it's responsible for, it pulls the task from Redis and starts processing it.
    <br>     
   4. Task Execution:
        - The Celery worker executes the task by calling the corresponding Python function defined in the tasks.py module.
        - For example, if the worker picks up the add task, it executes the add function with the provided arguments.
    <br>
   5. Task Completion:
       - After executing the task, the Celery worker may optionally store the result in the result backend (e.g., Django database or Redis) for later retrieval.
       - The result can include information about the task's success, failure, or any output generated during execution. 
       <br>
       <br>

**Comparison between @task and @shared_task**
   - **@shared_task**:
        - @shared_task is a higher-level decorator provided by Celery.
         <br>
        - It behaves similarly to @task but offers additional features and integration with Django.
         <br>
        - Use @shared_task when integrating Celery with Django projects or when you want the task to be discoverable and automatically registered with Celery.

           - **comparison between without bind=True and bind=True**
               - When bind=True is used in the @shared_task decorator, the task function receives the task instance as its first argument.
               - Flower relies on this task instance context to provide real-time status updates and detailed task information.
               - Without bind=True, the task function lacks direct access to task instance attributes, potentially limiting Flower's ability to display runtime status.
               - Therefore, using bind=True enhances visibility and provides more comprehensive task monitoring capabilities in Flower.
         <br>

   - **@task**:
       - @task is the lower-level decorator provided by Celery.
       <br>
       - It's a more basic decorator and doesn't provide the same level of integration with Django as @shared_task.
       <br>
       - Use @task when you're working with standalone Celery applications or when you want more control over task registration and behavior.



**Command to run celery: celery -A django_celery_project.celery worker -n worker_for_add_sub -Q add-queue,sub-queue -l INFO -P gevent**

- celery:
   - This is the command-line interface (CLI) for Celery, used to interact with Celery-related tasks and workers.
- -A django_celery_project.celery:
   - Specifies the Celery application to use. -A stands for "app" or "application".
   - In this case, django_celery_project.celery refers to the Celery application instance created in the celery.py module within the django_celery_project Django project.
- worker:
   - Indicates that this command will start a Celery worker process.
   - Celery workers are responsible for executing tasks that are sent to them via the message broker.
- -n worker_for_add_sub:
   - Specifies the name of the Celery worker.
    - Workers are identified by unique names, which can be  - - useful for monitoring and managing workers.
    - In this case, the worker is named worker_for_add_sub.
- -Q add-queue,sub-queue:
    - Specifies the queues that the worker should listen to for tasks.
    - The worker will only process tasks from the specified queues (add-queue and sub-queue in this case).
    - Queues allow you to organize tasks based on their type or priority.
- -l INFO:
     - Sets the logging level for the Celery worker.
     - In this case, the logging level is set to INFO, which means that informational messages will be logged.
     - Other possible logging levels include DEBUG, WARNING, ERROR, and CRITICAL.
- -P gevent:
     - Specifies the eventlet concurrency pool implementation to use.
     - In this case, -P gevent indicates that the worker will use the "gevent" pool, which is based on the gevent library.
     - The concurrency pool determines how tasks are executed concurrently within the worker process.

In summary, the celery command starts a Celery worker named **worker_for_add_sub**, which listens to the **add-queue** and **sub-queue** for tasks, uses gevent concurrency, and logs at the INFO level. This worker will execute tasks defined in the django_celery_project.celery application.


