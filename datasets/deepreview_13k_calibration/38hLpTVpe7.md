# Teaching Transformers Modular Arithmetic at Scale

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5

## Abstract
Modular addition is, on its face, a simple operation: given $N$ elements in $\mathbb{Z}_q$, compute their sum modulo $q$. Yet, scalable machine learning solutions to this problem remain elusive: prior work trains ML models that sum $N \le 6$ elements mod $q \le 1000$. Promising applications of ML models for cryptanalysis\textemdash which often involve modular arithmetic with large $N$ and $q$\textemdash motivate reconsideration of this problem. This work proposes three changes to the modular addition model training pipeline: more diverse training data, an angular embedding, and a custom loss function. With these changes, we demonstrate success with our approach for $N = 256, q = 3329$, a case which is interesting for cryptographic applications, and a significant increase in $N$ and $q$ over  prior work. These techniques also generalize to other modular arithmetic problems, motivating future work. % in this space.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a few techniques that promote faster convergence in learning modular addition with encoder-only transformers. The techniques include a slight modification of loss function, angular embedding of inputs and modifications of training distribution.

### Strengths
* The paper is mostly focused on experimental evaluation of different training strategies, and their experiments are well-detailed and reproducible. 
* The methodology proposed is well presented and easy to understand and follow.

### Weaknesses
### Major concerns:
* I don't understand why solving modular addition in scale is important. The other papers that the authors have cited and compared their work to use the setting of modular addition as a means of studying different behaviours of training algorithms or models. The authors mention that it is important in cryptography literature, but they never elaborate on how "learning to solve modular addition" with the given inputs is an important task. If we have the angular embeddings, or the integers, or even one-hot embeddings, then solving the task is straightforward.

* **Same setting having different results:** In table 7, the numbers of the bold row (N=20, q=257) are different from the numbers in the first row of Table 8. Don't these represent the exam same setting in running experiments? If so, where is the discrepancy coming from? This setting appears in other tables with other (different) numbers as accuracy as well, which is confusing.

* Section 5.4: If I understand correctly, Figure 5 claims to depict the PCA visualization of the outputs. IIUC, the targets are the angular embeddings of modular sums, the output dimension is 2. I don't see why PCA is needed here, since the output dim is already 2. Furthermore, when MSE is low, it's clear that the outputs must correspond to the angular embeddings of the targets and must be distributed on a circle, and when MSE is high they should not. I don't see how this tells us anything about the internal workings of the model.

* Overall, I think the techniques proposed require a practitioner to know about the structure of the problem (that we're going to solve a modular addition problem) and are not general beyond modular arithmetic. On the contrary, when we know that we're dealing with a modular addition problem, there are far superior approaches to solve the task than learning a deep network.

### Minor concerns:
* IIUC, Mohamadi et al's claim regarding the need for a fraction of data only applies to the so called "kernel-regime" where the network is not allowed to do any feature learning, and doesn't apply to trained networks. 
* For the cryptography use case that the authors have mentioned: does partial correctness (achieving non-trivial but also not 100% evaluation accuracy) matter in the mentioned use case? If not, how can one ensure 100% evaluation accuracy on a given task?

### Questions
I've mentioned my questions in the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper designs an architecture, representation, and dataset to use to train an encoder-only transformer model to perform modular addition of a fixed number of addends modulo a fixed prime.

### Strengths
The techniques used do improve performance on this problem, sometimes drastically, and indeed escape the symmetry-based lower bounds of Mohamadi et al. (2024) by using non-uniform sampling and representations which are not permutation-equivariant. This aligns somewhat with the results of Abbe et al. (2024).

Some of the analyses of the impacts of different decisions in the training process are quite interesting.

### Weaknesses
The paper presupposes that it is interesting to train an ML model to perform modular arithmetic in order to get good performance. I would vehemently argue, despite the existence of several recent paper which do train ML models to perform modular arithmetic (many of which I do think are quite interesting and with whose details I am very familiar), that this is not of any interest whatsoever. Here is a function far more interesting to cryptanalysis for this task: `lambda q, nums: sum(nums) % q`. This function achieves 100% accuracy for any `N` and `q`, probably runs _many_ orders of magnitude faster than your trained model with _far_ less memory, and doesn't require 240 GPU-hours of training.

So why is there so much recent work on training ML models to do modular arithmetic? This is _because_ it's such an easy problem, where we can understand what the network is doing when, e.g., exhibiting grokking behavior, or thinking about curriculum design, etc. The focus of these papers is not on obtaining the best learned model, but on what the process of learning on this toy problem can tell us about learning in general.

Thus, a paper about obtaining the best ML model to do modular arithmetic seems entirely misguided to me. A paper using modular arithmetic as a case study to investigate problems like curriculum/training distribution design, out-of-distribution generalization, etc could potentially be very interesting! There are a few parts of this paper that touch on things along these lines, and indeed the decisions about representation, the training distribution you use, etc are intriguing. But they're in service of a useless problem. I would suggest instead taking the kinds of decisions you made here to get things to work as an idea to explore in more general cases, taking modular arithmetic as a test case, rather than trying to get the best modular arithmetic network.

### Questions
- Is there a cryptanalytic application where a transformer implementing modular arithmetic, or something close to it, would be preferable to simply calling highly-optimized and accurate modular arithmetic routines?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The work considered learning modular addition via transformers at scale and proposed three changes to the modular addition model training pipeline for this purpose: 1) diversifying the training data; 2) an angular embedding, 3) a new loss function. The work showed that these changes lead to improvement for learning at scale, scaling up to N=256 elements modular q=3329. It also showed that these techniques generalize to other modular arithmetic problems (a few specific low degree polynomials modular q).

### Strengths
- The work investigated in detail the existing training methods on the problem, identified potential drawbacks, and proposed corresponding techniques to address them.
- The work provided empirical evidence that the proposed changes can help.

### Weaknesses
 - The problem addressed is quite limited: scaling up for a specific problem of modular addition tested over uniform distirbution. While the work provided some motivation, it is still unclear what's the impact of the work for future research/applications.
- It is unclear if the technical contributions are significant. The changes proposed are natural and not surprising. Furthermore, although the work tested on a few other modular arithmetic problems, those problems are specific and the evaluation is quite preliminary. It is unclear if the techniques can help for more general learning settings eg other algebraic reasoning tasks.

### Questions
- What about using active learning/sampling to generate training data? 
- The evaluation uses test data from a particular distribution (uniform). This is standard. But things can be different in applications. What if the test data (ie motivated via the cryptanalysis application mentioned in the intro) have a different distribution? How to adjust the techniques?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper tackles the challenge of enabling machine learning models, specifically transformers, to handle modular arithmetic with significantly larger values for \( N \) and \( q \) than previously studied. Traditional ML models struggle with modular arithmetic, particularly with parameters like \( N = 6 \) and \( q = 1000 \). This work proposes three key modifications that together enhance the performance of transformers on modular addition tasks:

1. **Enhanced Training Data Diversity**: By including a mix of simpler and rare modular addition examples, the authors aim to help the model generalize effectively.
2. **Angular Embedding**: This technique maps integers onto a unit circle, aligning better with the periodic nature of modular arithmetic.
3. **Custom Loss Function**: The authors introduce a specialized loss function designed to prevent convergence on local minima, ensuring that the model learns effectively.

These methods enable the transformer-based model to achieve high accuracy on modular addition tasks with values up to \( N = 256 \) and \( q = 3329 \), significantly surpassing prior results. The approach also shows potential for generalization across other modular arithmetic functions.

### Strengths
This paper’s key strengths lie in its innovative methodology and rigorous validation. The angular embedding and specialized loss function introduce solutions directly tailored to the demands of ML-based modular arithmetic. As modular arithmetic is foundational in cryptography, this work could help drive advancements in ML-powered cryptanalysis. The methodological rigor is enhanced by detailed ablation studies, and the inclusion of visualizations like PCA plots adds clarity, reinforcing the paper's accessibility and value.

### Weaknesses
While the proposed data distribution and loss modifications are effective, they add complexity. Discussing potential simplifications or alternative approaches for less resource-intensive implementation would be beneficial. While the model performs well up to \( N = 256 \) and \( q = 3329 \), addressing potential limitations as these parameters increase would add further depth. The claim that the model converges to a local minima at the origin is not entirely accurate, as the origin is not a local minimum in the traditional sense. The model's tendency to predict values close to (0,0) is more likely a consequence of the MSE loss function, which is minimized when the predicted values are close to the average of the target variable. Given the symmetric nature of sine and cosine around 0, the average target value is close to zero, leading the model to predict a constant value. This should be clarified to avoid misinterpretations about the optimization landscape. Additionally, the comparison with interpretability-focused works in Table 2 is not entirely relevant, as these works do not directly address the challenge of enhancing modular addition capabilities. This makes the comparison less meaningful and potentially misleading, as the focus of these works is fundamentally different.

### Questions
1. **Local Minima at the Origin**: You mention that the model can converge on local minima like the origin of the unit circle, which hinders learning. Since the correct output for a label \( x \) would be represented as \( \cos(2\pi x / q) \) and \( \sin(2\pi x / q) \), could you clarify why the origin (0,0) acts as a local minimum in this context? It would be helpful to understand how this specific point prevents effective training, given the angular nature of the embeddings.

2. **Digit-wise Tokenization for Modular Addition**: Have you experimented with digit-wise tokenization methods, such as representing numbers as sequences of digits, to evaluate how the model performs on modular addition tasks? It could provide insights into the model's ability to generalize on addition when individual digits are tokenized.

3. **Comparison with Interpretability-focused Work**: In Table 2, many of the related works primarily address interpretability aspects rather than modeling improvements for modular addition. This focus makes direct comparison potentially less relevant. Could you elaborate on why these specific interpretability-focused works were chosen, and consider whether it might be beneficial to compare primarily with approaches that directly aim to enhance modular addition capabilities?

4. **Comparison with Other Embedding Techniques**: Given that you propose a new embedding and custom loss, it would be helpful to see how it compares with existing methods designed for modular arithmetic or general embedding approaches, such as abacus embedding (https://arxiv.org/abs/2405.17399) or dice embedding (https://aclanthology.org/2020.emnlp-main.384.pdf). Have you tried these methods, and if so, how did they perform relative to your angular embedding? This comparison could add further depth to your evaluation of embedding strategies in modular arithmetic tasks.

### Soundness
4

### Presentation
3

### Contribution
2
