# Breaking Free from MMI: A New Frontier in Rationalization by Probing Input Utilization

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Extracting a small subset of crucial rationales from the full input is a key problem in explainability research. The most widely used fundamental criterion for rationale extraction is the maximum mutual information (MMI) criterion. In this paper, we first demonstrate that MMI suffers from diminishing marginal returns. Once part of the rationale has been identified, finding the remaining portions contributes only marginally to increasing the mutual information, making it difficult to use MMI to locate the rest. In contrast to MMI that aims to reproduce the prediction, we seek to identify the parts of the input that the network can actually utilize. This is achieved by comparing how different rationale candidates match the capability space of the weight matrix. The weight matrix of a neural network is typically low-rank, meaning that the linear combinations of its column vectors can only cover part of the directions in a high-dimensional space (high-dimension: the dimensions of an input vector). If an input is fully utilized by the network, it generally matches these directions (e.g., a portion of a hypersphere), resulting in a representation with a high norm. Conversely, if an input primarily falls outside (orthogonal to) these directions, its representation norm will approach zero, behaving like noise that the network cannot effectively utilize.  
Building on this, we propose using the norms of rationale candidates as an alternative objective to MMI. 
Through experiments on four text classification datasets and one graph classification dataset using three network architectures (GRUs, BERT, and GCN), we show that our method outperforms MMI and its improved variants in identifying better rationales. We also compare our method with a representative LLM (llama-3.1-8b-instruct) and find that our simple method gets comparable results to it and can sometimes even outperform it.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
+ The paper first identifies an issue of current MMI methods: once part of the rationales are detected, it is hard to find the remaining parts due to diminishing marginal returns.

+ Targeting this issue, the paper empirically analyzes the norm of the rationale's representation in the training process, considering the relationship between the information richness and the representation norm.
+ Based on the analysis results, the paper proposes to use/add the log representation norm to the Extractor's training loss, and the proposed method achieves better performance compared to several baselines.

### Strengths
+ The identified issue of current MMI methods is meaningful and insightful.
+ The proposed method makes sense intuitively. It is also a simple way to tackle the identified issue and seems to be effective.

### Weaknesses
 + Missing some key evaluation results
  + What's the accuracy of the Predictor (i.e., task accuracy) if taking as input the rationale extracted by BERT-based methods and llama-3.1-8b-instruct?
  + Why did you evaluate BERT-based methods on ONLY Beer-Appearance? Is there any specific reason for not showing results on the other three datasets?
+ It would be better to study what the improvement in the numbers actually means. Humans may have very different annotations when asked to extract a rationale. For instance, in the toy example (line 266), I personally prefer taking only R2 as the rationale as it is quite enough to make the prediction (and thus I can give a more concise rationale than R1+R2). Therefore, it is unclear whether the number improvement really means a better rationale (e.g., a rationale that avoids missing information that is actually essential). One possible way is to do some case study or human analysis to compare rationales extracted by different methods.
+ Comparing Table 1 and Table 3, I found that BERT-based methods (i.e., taking BERT as the encoder) seem to perform worse than GRU-based methods on Beer-Appearance. It is not intuitive for me as BERT is expected to be a stronger model. Do you have any explanations?

### Questions
+ Comparing Table 1 and Table 3, I found that BERT-based methods (i.e., taking BERT as the encoder) seem to perform worse than GRU-based methods on Beer-Appearance. It is not intuitive for me as BERT is expected to be a stronger model. Do you have any explanations?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work suggests extracting crucial rationales from an input of language models using the weight matrices of these language models. The proposed method is an alternative to the more traditional MMI method. It should help us move towards more explainable AI by showing which parts of the input are crucial for making a decision.

### Strengths
- The work investigates an important topic: XAI.
- Authors repeat each experiment several times and report standard deviation.

### Weaknesses
It is very hard to understand the contribution:

- The method description in abstract, introduction and many other places of the paper seems to be simply wrong. Weight matrices of LLMs (excluding "attention weights"; but the paper doesn't tell anything about attention weights) are not dependent on the particular input, so they can not be used for estimating the parts of inputs. The method description in the paper should be rewritten completely.

- I suppose that the authors could mean components of the embedding matrix, not the weight matrix? But this suggestion still leads to confusion: I looked into the code and it still wasn't clear how exactly the model's embeddings were used in calculations. E.g. the function "`get_embeddings`" from embeddings.py is not used in other scripts at all. At the same time, "`get_glove_embedding`" function was used; but there is not even a single mention of GloVe in the paper itself, so there is a contradiction again. I urge the authors to make their code more clear and consistent with the paper text.

- The reasoning about the rank of "weight matrices" also sounds unclear and not founded enough. It is again unclear, whether weight matrices or embedding matrices are considered; besides, in the context of neural networks, it is hardly possible to talk about "zero matrix rank" for sure in any case. In a strict sense, "zero rank" would mean that the whole matrix is exactly zero which is very rare case in practice. Probably authors mean some approximation of the matrix rank, but the exact formula for that approximation was never written down.

- Figure 2 doesn't look correct, it's meaning is unclear (see "Questions" part). Its description also looks unclear and not founded enough.

Other issues:

- If we assume again that authors mean embeddings and not weight matrices (as follows from common sense and from "4.2 The practical method" part of the paper), it is still not clear, what will happen if the input isn't connected to the task at all. E.g. if the input is like "John went for a walk", and the task is to estimate, whether he liked the beer aroma or not. It seems that the suggested approach (or, at least, my, very vague understanding of it), isn't able to correctly handle such situations.

Minor issues:

- Citations in lines 167-173 should be put into braces.

### Questions
- What does x axis of Figure 2 mean?
- What do notations in Equation 2 mean? (they are not defined in the text)

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The study introduces an alternative approach to Maximum Mutual Information (MMI) for extracting rationales in explainable AI (XAI). Traditionally, MMI-based methods have been used to extract relevant features by maximizing information shared between input rationales and predictions. However, the authors argue that MMI suffers from diminishing marginal returns, limiting its efficacy in fully capturing critical rationale components. They propose using the norms of input representations, aligning extracted rationales with utilized parts of the network's weight matrix. This novel method Norm to Rationale (N2R), reportedly outperforms MMI-based methods across several datasets (text and graph-based). Authors use GRUs, BERT and GCN as an encoders, and several text classification and one graph classification dataset.

### Strengths
- The use of encoder output norms for rationale extraction is novel, and the experiments provide convincing motivation for using this approach over MMI-based methods.
- The theoretical analysis of MMI-based methods is clear and engaging.
- The proposed method is promising due to its simplicity and potential for generalizability.
- The authors conduct experiments with multiple random seeds and report results with standard deviations, which significantly improves the rigor of the work and reinforces confidence in the performance of the approach.

### Weaknesses
 - The experiments are limited to datasets with annotated rationales, and the authors do not present results showing how their approach improves classification quality in more advanced real-world datasets.
- The experiments focus solely on text and graph domains. The claim of generalizability would be strengthened by including additional domains. Specifically, the method's applicability to domains with high dimensionality or complex data structures, such as time-series data or 3D point clouds, remains unexplored. This limits the assessment of the method's robustness and broad applicability.
- The impact of norm-based rationale selection on computational resources, particularly for larger models, is not discussed. Additionally, the authors omit details and experiments regarding the properties of the encoder and extractor, such as whether the encoder should have a specific architecture or how scaling the encoder affects the method. For instance, the effect of using different activation functions or normalization layers within the encoder on the extracted rationales is not investigated. Furthermore, the method's sensitivity to the depth and width of the encoder network is unclear.
- While the empirical results are compelling, the theoretical foundation for norm-based rationale extraction could benefit from additional depth. More detailed mathematical insights into why norms better capture input utility and how the input interacts with the encoder's weight matrix could strengthen the approach. Specifically, a formal analysis of the relationship between the norm of the encoder output and the information content of the input, perhaps using concepts from information theory, would be beneficial. The current justification lacks a rigorous mathematical framework.

### Questions
I find the approach interesting, but I have a few questions and suggestions that could further improve the study:

- How does this approach actually improve classification quality in real-world scenarios? The paper mentions MMI limitations, but do these truly impact final performance? I understand that classification performance isn’t the primary goal of explainable AI, but it would be interesting to see if there’s a noticeable effect.
- You claim generalizability across domains, yet the experiments are limited to text and graphs. Could this method be extended to other domains, such as speech or even image classification?
- It is unclear if there are specific limitations regarding encoder and extractor architectures. Could you clarify this? Additionally, it would be interesting to see how the approach scales with (a) an increasing number of encoder parameters and (b) longer input text lengths. I believe such experiments would enhance the work, making it more valuable for tasks like in-context learning and RAG prompt improvements.

Minor Remarks and Questions:

- It is unclear why you use the logarithm in Eq. (8) and subsequent equations. Is this related to Fig. 3c?
- Figure 3 is somewhat confusing: there are no y-labels, and the caption lacks references to panels (a), (b), and (c).
- Figure 2 appears after Figure 3; it may be better to reorder them for clarity.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors propose a novel approach for extracting rationales in a select-predict-like pipeline, replacing the traditional MMI loss criterion  with a new objective that is independent of the output prediction.

They claim that MMI suffers from diminishing marginal returns, that is, the model can select a portion of the input as rationales and still predict the true label with insignificantly lower accuracy.

Therefore, instead of relying on the output prediction for evaluating the rationales extraction, they prob the weight matrix of neural networks norm to detect snippets that the model truly utilize.

### Strengths
- Model agnostic method (They propose a new metric for rationale extraction which is regardless of the model itself as long as you have access to the weights).
- Their method falls in the self-explanation category which guarantees faithful rationales.
- Potential to be extended to image classification and graph neural network.
- Mixing N2R and MMI improves the performance even better as MMI works better in the early stages of finding rationales and N2R works better when the models already detected few.

### Weaknesses
 - Works like UNIREX already discussed the problem you mentioned about MMI by introducing "sufficiency" and "comprehensiveness" metrics.
- The extractor and the predictor are not trained cooperatively (end-to-end) due to the non-differentiability of rationale space.
- You should put the task performance in the results. 
- Visualization of some extracted rationale would be great.
- You didn't provide the hyperparameter (for example in Eq. 5) in your experiments.

### Questions
- I was wondering what are the metrics when you pass gold rationales to the predictor directly. This would indicate the maximum performance you could reach.
- I was wondering what is the performance of your framework w.r.t. OOD data. This helps to understand if the model learn to rely on plausible rationales instead of statistical shortcuts
- BeerAdvocate is more sentence level rationales, evaluating on token level rationales (like e-SNLI) which is more challenging would be interesting.

### Soundness
3

### Presentation
4

### Contribution
2
