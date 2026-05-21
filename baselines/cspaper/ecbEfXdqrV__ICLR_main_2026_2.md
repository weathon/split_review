---
job_id: 75639b4d-94ad-4161-b4ef-291266efdb70
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: ecbEfXdqrV.pdf
paper: Why Is the Counterintuitive Phenomenon of Likelihood Rare in Tabular Anomaly Detection with Deep Generative Models?
main_score_norm: N/A
desk_reject: true
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on generative models, likelihood-based anomaly detection, and theoretical/empirical analysis of deep normalizing flows.

## Minimum Quality
Fail ❌. While the paper has the expected structure and is broadly relevant, the experimental methodology has a fatal flaw: the main evaluation uses test-set performance for hyperparameter/model selection. On **Page 5**, the paper states that after running all hyperparameter combinations with repeated experiments, “the hyperparameter combination with the highest average AUROC for all datasets is selected,” which means the reported benchmark results are selected using test AUROC across the benchmark. This is a form of test-data-driven model selection and undermines the validity of the empirical claims.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find evidence in the paper text of hidden prompts, instructions targeting automated reviewers, or other manipulative content.