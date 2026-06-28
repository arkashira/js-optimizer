# Tech Spec: js-optimizer
=====================================

## Stack
---------------

* **Language**: JavaScript (ES6+)
* **Framework**: None (library-based)
* **Runtime**: Node.js (14.x+)
* **Rust**: Used for compilation and optimization (via SWC)
* **SWC**: Used for JavaScript compilation and optimization

## Hosting
------------

* **Free-tier-first**: Hosted on AWS Lambda (500k free requests/month)
* **Specific platforms**: Also deployable to Vercel (formerly Zeit Now) and Netlify

## Data Model
--------------

### Tables/Collections

* **Optimization Jobs**: stores information about ongoing and completed optimization jobs
	+ `id` (string, primary key): unique job ID
	+ `input` (string): input code for optimization
	+ `output` (string): optimized code
	+ `status` (string): job status (e.g. "pending", "running", "completed")
	+ `created_at` (timestamp): job creation timestamp
	+ `updated_at` (timestamp): job update timestamp

## API Surface
----------------

### Endpoints

1. **POST /optimize**
	* Purpose: Start a new optimization job
	* Method: POST
	* Path: `/optimize`
	* Request Body: `input` (string): input code for optimization
	* Response: `200 OK` with `output` (string): optimized code
2. **GET /jobs**
	* Purpose: Retrieve a list of ongoing and completed optimization jobs
	* Method: GET
	* Path: `/jobs`
	* Response: `200 OK` with `jobs` (array of objects): list of optimization jobs
3. **GET /jobs/{id}**
	* Purpose: Retrieve a specific optimization job
	* Method: GET
	* Path: `/jobs/{id}`
	* Response: `200 OK` with `job` (object): optimization job details
4. **DELETE /jobs/{id}**
	* Purpose: Cancel an ongoing optimization job
	* Method: DELETE
	* Path: `/jobs/{id}`
	* Response: `204 No Content`
5. **GET /health**
	* Purpose: Check the health of the service
	* Method: GET
	* Path: `/health`
	* Response: `200 OK` with `status` (string): service status (e.g. "healthy", "unhealthy")
6. **GET /metrics**
	* Purpose: Retrieve metrics about the service
	* Method: GET
	* Path: `/metrics`
	* Response: `200 OK` with `metrics` (object): service metrics

## Security Model
-----------------

### Authentication

* **API Key**: required for all API requests
* **IAM**: uses AWS IAM for role-based access control

### Secrets

* **Environment Variables**: uses AWS Secrets Manager for storing sensitive data

### Authorization

* **Role-Based Access Control**: uses AWS IAM for role-based access control

## Observability
----------------

### Logs

* **CloudWatch Logs**: stores logs in AWS CloudWatch Logs
* **Log Level**: logs at INFO level by default

### Metrics

* **CloudWatch Metrics**: stores metrics in AWS CloudWatch Metrics
* **Metric Prefix**: uses `js-optimizer` as the metric prefix

### Traces

* **AWS X-Ray**: uses AWS X-Ray for distributed tracing

## Build/CI
------------

* **CI/CD Pipeline**: uses GitHub Actions for CI/CD pipeline
* **Build Command**: `npm run build`
* **Test Command**: `npm run test`
* **Deployment Command**: `npm run deploy`