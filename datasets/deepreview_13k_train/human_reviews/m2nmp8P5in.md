# LLM-SR: Scientific Equation Discovery via Programming with Large Language Models

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Mathematical equations have been unreasonably effective in describing complex natural phenomena across various scientific disciplines. However, discovering such insightful equations from data presents significant challenges due to the necessity of navigating extremely high-dimensional combinatorial and nonlinear hypothesis spaces. Traditional methods of equation discovery, commonly known as symbolic regression, largely focus on extracting equations from data alone, often neglecting the rich domain-specific prior knowledge that scientists typically depend on. To bridge this gap, we introduce \modelname, a novel approach that leverages the extensive scientific knowledge and robust code generation capabilities of Large Language Models (LLMs) to discover scientific equations from data in an efficient manner. Specifically, \modelname treats equations as programs with mathematical operators and combines LLMs' scientific priors with evolutionary search over equation programs. The LLM iteratively proposes new equation skeleton hypotheses, drawing from its physical understanding, which are then optimized against data to estimate skeleton parameters.
We demonstrate \modelname's effectiveness across three diverse scientific domains, where it 
discovers physically accurate equations that provide significantly better fits to in-domain and out-of-domain data compared to the well-established symbolic regression baselines.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces LLM-SR, a new approach to discovering mathematical equations from data using LLMs' scientific knowledge and code generation. LLM-SR treats equations as program structures. LLM-SR achieves significant improvements over baseline symbolic regression methods.

### Strengths
1. Innovative approach: It is innovative to use LLMs for scientific equation discovery and symbolic regression. LLM-SR integrates LLMs' prior scientific knowledge and and code generation ability to achieve good performance.

2. Robust evaluation: The authors have carefully designed benchmark problems that align well with the real-world applications.

3. Comprehensive analysis: The qualitative analysis effectively evaluates the model's OOD generalizability  and the ablation study provides insight into the contribution of each of model's component.

4. Well written: The paper is well written with clear data presentation.

### Weaknesses
The paper does not provide detailed insight into how LLM-SR handles edge cases, such as noisy data, or highly complex functions. This could be important for real-world applications where data may be imperfect or equations are inherently intricate.

### Questions
1. A more thorough analysis of the computational cost, especially comparing LLM-SR to traditional symbolic regression techniques, would help gauge the practical feasibility of this approach.

2. Providing a real-world example of how LLM-SR assists in scientific problem solving could make the results more compelling.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces **LLM-SR**, a novel framework for discovering scientific equations using **Large Language Models (LLMs)**. The approach integrates LLMs' scientific knowledge and code generation capabilities with evolutionary search and optimization techniques to generate, evaluate, and refine mathematical equation hypotheses iteratively. The key steps involve generating equation skeletons, optimizing parameters using Python-based tools, and managing an experience buffer to iteratively improve the search process.

**Main Contributions:**
1. **Novel Framework**: LLM-SR combines LLMs' strengths with evolutionary algorithms to navigate complex equation discovery.
2. **Integration of Scientific Priors**: The method leverages LLMs' embedded scientific knowledge for more efficient hypothesis generation.
3. **Benchmark Creation**: The authors design new benchmark problems in physics, biology, and materials science to test the method's capabilities and avoid memorization of well-known equations.
4. **Performance Advantage**: LLM-SR reportedly outperforms traditional symbolic regression methods, showing better accuracy and generalization, especially in out-of-domain tests.
5. **Ablation Study**: Demonstrates the importance of various components, such as problem specification and iterative refinement, in the overall performance of LLM-SR.

### Strengths
1. **Innovative Application of LLMs for Scientific Equation Discovery**:
   - The authors introduce an innovative approach by leveraging the scientific knowledge and code generation capabilities of large language models (LLMs) for equation discovery. Representing equations as code and integrating data-driven feedback and optimization provides a novel perspective for scientific modeling.

2. **Experience Buffer and Iterative Optimization**:
   - The use of an experience buffer to maintain high-quality equation examples and facilitate iterative optimization is a unique feature. This mechanism helps the model learn and recall effective generation patterns, improving the quality and efficiency of equation exploration.

3. **Comprehensive Multi-Domain Benchmarking**:
   - The paper demonstrates the method’s applicability across multiple scientific domains, including physics, biology, and materials science. The newly designed benchmarks, which aim to prevent memorization of known equations, reflect the authors' commitment to scientific rigor.

4. **Promising Experimental Results**:
   - Despite certain challenges and areas for improvement, LLM-SR shows promising performance compared to existing symbolic regression methods, particularly in out-of-domain tests. This indicates potential for tackling complex scientific problems and suggests a valuable direction for future research.

### Weaknesses
 **Complexity and Necessity of the Method**:
The authors introduce complex mechanisms such as sampling strategies and an island model, showcasing innovative efforts. However, clearer justification is needed to explain the necessity of these elements and their specific contributions to enhancing the method’s performance. Simplifying and elucidating these mechanisms' actual benefits would improve the clarity and persuasiveness of the method.

**Utilization and Verification of Prior Knowledge**:
Although the authors assume that the LLM leverages its scientific prior knowledge to generate reasonable equations, the paper lacks detailed analysis and experimental validation of how this mechanism functions and its tangible effects. Further exploration and evidence would more convincingly support this claim and make the method’s core advantage clearer to readers.

**Breadth and Realism of Experimental Design**:
The current experiments are based on data generated from known equations, providing a basic evaluation. However, data in real-world scientific research often contains noise and outliers, and the method’s performance under such conditions is a critical indicator of its practical applicability. Including datasets with measurement errors and outliers would help demonstrate the method’s robustness and generalizability in complex, realistic scenarios.

**Impact of Programming Capabilities on Experimental Results**:
The paper emphasizes the LLM's ability to generate programming code but lacks analysis of whether these programming capabilities interfere with the experimental results. The boundary between the LLM’s programming skills and scientific reasoning remains unclear, which might mean that experimental outcomes reflect coding proficiency rather than pure scientific inference. Clarifying the role of these aspects in equation generation would aid in better understanding the method’s true strengths and limitations.

### Questions
1. **Clarification on the Necessity of Complex Mechanisms**:
   - *Question*: Could the authors elaborate on the rationale behind incorporating complex mechanisms such as the sampling strategy and island model? How do these elements contribute to the overall performance, especially compared to simpler alternatives?
   - *Suggestion*: Including comparative results or ablation studies that illustrate the impact of these mechanisms on the method’s performance would be helpful to better understand their necessity and specific contributions.

2. **Verification of LLM Prior Knowledge Utilization**:
   - *Question*: How do the authors verify that the LLM’s embedded scientific prior knowledge is effectively utilized during the equation generation process? Are there examples or analyses demonstrating cases where this prior knowledge played a significant role?
   - *Suggestion*: We suggest adding controlled experiments that isolate and assess the contribution of prior knowledge. Comparing models with and without domain-specific pretraining might further strengthen this aspect.

3. **Evaluation on Real-World Datasets with Noise and Outliers**:
   - *Question*: Do the authors plan to evaluate LLM-SR on more challenging, real-world datasets that contain noise, outliers, or measurement errors? How do they foresee the method performing under such conditions?
   - *Suggestion*: Expanding the experiments to include data with inherent noise and outliers, or discussing the method’s anticipated robustness in these cases, could help demonstrate its applicability to complex, real-world scenarios.

4. **Impact of LLM Programming Performance on Results**:
   - *Question*: Have the authors considered examining the extent to which the LLM’s programming capabilities, rather than scientific reasoning, might influence the results? How do they ensure that the outcomes reflect genuine equation discovery rather than sophisticated code generation?
   - *Suggestion*: Providing an analysis or qualitative examples that differentiate between the model’s programming skills and its scientific reasoning in generating equations would be valuable to clarify the contributions and limitations of the approach.

5. **Interpretability of Results**:
   - *Question*: The authors state that the generated equations are more interpretable and scientifically meaningful. Could they provide examples or a detailed comparison showing how LLM-SR’s output stands out in terms of interpretability relative to baseline methods?
   - *Suggestion*: Presenting case studies or examples where the equations discovered by LLM-SR provide clearer or more scientifically insightful interpretations would reinforce this claim.

6. **Broader Comparison with Hybrid Methods**:
   - *Question*: How does LLM-SR compare with recent hybrid approaches that incorporate domain knowledge or leverage deep learning for symbolic regression? Are there particular strengths or limitations of LLM-SR compared to these methods?
   - *Suggestion*: Including comparisons with other state-of-the-art hybrid methods or discussing potential improvements and challenges in adapting LLM-SR could provide more context on its positioning and competitive advantages.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a method for symbolic regression (SR) that combines LLM-based evolutionary search for program synthesis with numerical optimizers (such as BFGS and Adam) to tune the parameters of the generated programs. The authors, additionally, present four new SR problems that were created with synthetic modifications to address concerns regarding LLM memorization. Finally, ablations are provided to analyze the benefits of different design choices.

### Strengths
1. To the best of my knowledge, framing SR as equation _template_ discovery seems novel and a useful contribution.
2. The analyses presented to demonstrate LLM memorization of the Feynman dataset are quite convincing.
3. The new benchmark problems are well-motivated and look like sound contributions.
4. The paper is, overall, clearly written and easy to follow, and visualizations are used well in various places.

### Weaknesses
My main concerns with the work are twofold:
1. The paper reads in a manner that moderately overclaims novelty. The main idea appears to be the combination of numerical optimizers with LLM-based optimization over templates, besides the contribution of new SR problems. However, the motivation, currently, is primarily devoted to comparisons with non-LLM methods, which seems unfair. Since the framing of SR problems within the context of LLM-based optimization is not new (Table 1 from [1] is a useful reference), it would be more appropriate to motivate the work by describing existing LLM-based SR methods, clearly stating their problems, and then showing how the new method addresses them.  
2. My second concern is regarding the choice of baselines. While I appreciate the inclusion of several standard SR methods, I think the comparisons do not precisely show the benefits of the paper's contributions.  
  (a) Given prior works such as [1, 2, 3] in LLM-based SR/optimization, it would have provided utility to see the performance of the proposed method in comparison to its closest counterparts. Alternatively, if the argument is that some of the ablations subsume these methods, it would then be useful to see those ablations presented as the main baselines on all the datasets instead of only on a partial set.  
  (b) The ablation results from Figure 6 show that a substantial drop in performance occurs when coefficient optimization is removed. Based on this, it would have been useful to see whether simply equipping the non-LLM baselines with a similar coefficient optimizer would close the gaps that we currently see in Table 1. I am currently not convinced that the LLM is needed to facilitate the evolutionary search of equation templates.  

Minor:
1. The choice of describing the contents in Section 2.4 as "Experience Management" is mildly concerning. Given a large body of prior work in evolutionary computation, it would be appropriate to avoid fragmenting the literature for the benefit of differentiation and instead re-use existing terminology. If there is indeed an aspect that warrants a new term, please do correct me.  
2. It was mildly odd to read that mathematical equations have been "unreasonably" effective in describing complex phenomena. Unclear why we think it is unreasonable.  

### Questions
1. L243 briefly described how population initialization is performed. Is the linear equation skeleton manually written? How many skeletons are provided at initialization?  
2. In L149, should the expectation be over the data points in $\mathcal{D}$?  
3. In Appendix E, could you clarify what LLM-SR (w/o Prior) refers to? From the text described in the main paper, I could not find mention of the described "problem-specific prior knowledge" (L1220).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents LLM-SR (Large Language Model Symbolic Regression), a framework that employs LLMs to discover scientific equations by treating equations as programs. LLM-SR combines LLMs with evolutionary search techniques to generate, evaluate, and refine equations that describe complex scientific phenomena. The process includes hypothesis generation by the LLM, parameter optimization of proposed equations, and a dynamic experience management system to refine hypotheses iteratively. The authors demonstrate LLM-SR’s superior ability to discover accurate and generalizable equations compared to traditional symbolic regression methods, especially in out-of-domain settings.

### Strengths
1. The approach of using LLMs to generate symbolic equation structures combines programming and scientific prior knowledge, setting it apart from traditional symbolic regression methods.
2. LLM-SR shows strong performance not only in-domain but also in out-of-domain scenarios, which is often challenging for symbolic regression techniques.
3. By leveraging scientific prior knowledge and a structured experience buffer, LLM-SR reduces the search space, achieving good results with fewer iterations compared to traditional methods.

### Weaknesses
1. The framework relies heavily on the embedded scientific knowledge of LLMs, which may be biased, incomplete, or inaccurate for certain scientific domains, potentially limiting its robustness. This dependence on pre-existing knowledge within the LLM could lead to a confirmation bias, where the model favors equations that align with its internal representations, rather than exploring novel or unexpected relationships in the data. The lack of a mechanism to explicitly validate or correct the LLM's scientific priors could lead to the propagation of errors, especially in less-explored domains.
2. Although the paper addresses different domains, it would benefit from more diverse and complex real-world datasets to further validate the method’s general applicability. The current datasets, while varied, may not fully capture the intricacies and noise present in many real-world scientific problems. The absence of datasets with high levels of noise, missing data, or complex non-linear interactions limits the ability to assess the robustness and scalability of the proposed method.

### Questions
1. How would LLM-SR perform with even larger LLMs or specialized scientific models?
2. How does LLM-SR perform with complex systems involving interactions across multiple equations?

### Soundness
3

### Presentation
3

### Contribution
3
