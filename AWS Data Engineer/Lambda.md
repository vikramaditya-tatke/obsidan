Serverless, used for executing code snippets and continuous scaling.

- Used as an intermediary between various data services.
- Transformation jobs, such as receiving data from Kinesis Data Streams, transforming it and sending it back or to a data warehouse.
- In the context of using Lambda with streaming services like Kinesis Data Streams and MSK, these services CANNOT write the data into Lambda. **Instead Lambda polls these services periodically.**
## Example: Serverless Website

![[Excalidraw/Lambda Serverless Website]]

## Lambda Triggers

![[Pasted image 20251101200028.png]]