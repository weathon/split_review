# HADAMRNN: BINARY AND SPARSE TERNARY ORTHOGONAL RNNS

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Binary and sparse ternary weights in neural networks enable faster computations and lighter representations, facilitating their use on edge devices with limited computational power. Meanwhile, vanilla RNNs are highly sensitive to changes in their recurrent weights, making the binarization and ternarization of these weights inherently challenging. To date, no method has successfully achieved binarization
or ternarization of vanilla RNN weights. We present a new approach leveraging the properties of Hadamard matrices to parameterize a subset of binary and sparse ternary orthogonal matrices. This method enables the training of orthogonal RNNs (ORNNs) with binary and sparse ternary recurrent weights, effectively creating a specific class of binary and sparse ternary vanilla RNNs. The resulting ORNNs, called HadamRNN and Block-HadamRNN, are evaluated on benchmarks such as the copy task, permuted and sequential MNIST tasks, and IMDB dataset. Despite binarization or sparse ternarization, these RNNs maintain performance levels comparable to state-of-the-art full-precision models, highlighting the effectiveness of our approach. Notably, our approach is the first solution with binary recurrent weights capable of tackling the copy task over 1000 timesteps.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a method to parameterize the recurrent weights of Orthogonal Recurrent Neural Networks (ORNN), a special case of Vanilla RNN to binary or sparse ternary matrices. The binarization and sparse ternarization algorithms that the paper proposed are based on Hadamard Matrix Theory. The paper tests the algorithms on two types of binarized and sparse ternarized Orthogonal Vanilla Recurrent Networks and compares their performance to LSTMs and GRUs recurrent models for four standard benchmark datasets.

### Strengths
The paper proposes a novel approach to parameterize weights of Orthogonal RNN models using Hadamard Matrix Theory. As mentioned in the paper the binary and sparse ternary parameterization are investigated and analyzed on lightweight neural networks for time series, the results reported in Table 2 highlight the potential of the proposed approach by comparing to ORNN, LSTM and FastGRNN recurrent models.

### Weaknesses
The binarization and ternarization algorithms of Orthogonal Vanilla RNN are explained in sections 3.3 and 3.4 in a high-level way. Maybe providing a base example by giving the dimensions of the matrices to be binarized or ternarized would make the algorithms more transparent and easy to understand. 

The results reported in Table 2 and Table 3 are tough to read. Maybe converting some of the results into plots would make it more straightforward for the reader to assess the paper's contributions. It is unclear where the advantage of using Hadamard Matrix Theory to parameterize the binary orthogonal recurrent weights lies.
The paper does not analyze the method proposed on any edge device. Reporting the overhead and the speedup obtained on HadamardRNN and Block-HadamardRNN would help assess the paper's contribution.

### Questions
- Could you evaluate the performance of Block-HadamRNN and HadamRNN on edge devices? In particular, would you be able to provide the speedup and computational overhead that while using your techniques on these devices?

- Could you maybe think about making Tables 2 and 3 simpler to improve the readability of your results? Better visual perception may also result from the inclusion of a plot that contrasts the accuracy of all the suggested and benchmark approaches.

- Could you maybe include a thorough example in the text that shows how a trained ORNN is subjected to the binarization or sparse ternarization algorithms? Could you also explain the Straight-Through Estimator's (STE) function in the parameterization process?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Binary and sparse ternary weights in neural networks enable faster computations and lighter representations, facilitating their use on edge devices with limited computational power. However, to date, no method has successfully achieved binarization or ternarization of vanilla Recurrent Neural Network (RNN) weights. As a result, in this paper, the authors present a new approach leveraging the properties of Hadamard matrices to parameterize a subset of binary and sparse ternary orthogonal matrices. The method enables the training of Orthogonal RNNs (ORNNs) with binary and sparse ternary recurrent weights, effectively creating a specific class of binary and sparse ternary vanilla RNNs. Despite binarization or sparse ternarization, the proposed RNNs maintain performance levels comparable to state-of-the-art full-precision models, highlighting the approach's effectiveness.

### Strengths
The paper is well-organized and has a high level of clarity in its writing and the presentation of its proposal.

Each section flows logically, enhancing the reader's comprehension of the paper's purpose and methodology. Notably, sections 3 (+ the Appendix) stand out for its depth and precision, guiding the reader through the formality of the proposed approach and leaving little room for ambiguity regarding the study's methods and objectives.

The proposal is interesting. Although it is presented explicitly for RNN, the underlying principles and approaches have strong adaptability potential. The proposed sparse ternary orthogonal recurrent weights could be effectively applied across various domains (with necessary modifications for the new application domain).

### Weaknesses
My major concern with this paper is regarding the experimental section. Specifically, in lines 123 - 125, the authors claim: *"Even with binarization, transformer models [...], making them unsuitable for tasks involving long-term dependencies on edge devices."* I find this assertion to be overly restrictive, as recent literature provides a substantial body of work on optimizing Transformers for edge devices and handling long-term dependencies, which is not discussed here. For example, numerous studies have been conducted on lightweight binary Transformers [1, 2, 3, 4] and approaches specifically designed to handle long-term dependencies [5, 6, 7]. Consequently, the state-of-the-art section also appears narrow, as it overlooks several relevant studies and advancements in Transformer models that are critical to this discussion.

Specifically, the claim that binarized transformers are unsuitable for long-term dependencies on edge devices is not sufficiently supported. While it is true that naive binarization can lead to performance degradation, recent research has demonstrated methods to mitigate this issue. For instance, techniques like knowledge distillation, modified activation functions, and specialized training regimes have shown promise in maintaining accuracy while reducing the computational footprint of transformers. The paper should acknowledge these advancements and provide a more nuanced perspective on the applicability of binarized transformers in edge computing scenarios. The current state-of-the-art section lacks a comprehensive discussion of these techniques, which is a significant oversight.

Furthermore, the experimental section focuses solely on RNNs, neglecting a direct comparison with these optimized transformer models. This omission makes it difficult to assess the true novelty and practical relevance of the proposed approach. A more thorough experimental evaluation should include a comparative analysis against state-of-the-art binarized or otherwise compressed transformers, particularly those designed for long-term dependency tasks. Without such a comparison, the paper's claims of superiority in edge computing scenarios remain unsubstantiated. The lack of such a comparison is a significant weakness that needs to be addressed.

### Questions
Summarizing: The proposal is interesting. However, the weaknesses presented in terms of state-of-the-art and comparison are not so minor. Therefore, this work needs more effort to be improved, and it is not ready for publication in this state.

Based on the above, expanding the experiments and the related work to include additional competitors from Transformer-based models would significantly strengthen the paper's relevance and situate it better within the current research landscape.

Other minor considerations: I recommend that the authors carefully re-read the work; there are several typos and English errors. Furthermore, the plots in the Appendix do not specify what the X-axis and Y-axis represent.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper tackles the challenge of binarizing orthogonal recurrent neural networks (oRNNs), a problem that has been hindered by instability and inconsistency in previous formulations. The authors propose HadamRNN, a novel approach that utilizes Hadamard matrices to parameterize oRNNs with binary and sparse ternary weights. This method cleverly addresses the instability issues and offers a consistent framework for binarizing oRNNs. Furthermore, the paper introduces an optimized block version of HadamRNN, which brings about computational efficiency.

### Strengths
1) Novel Approach: The introduction of Hadamard matrices for parameterization is a novel and effective way to address the instability issues associated with binarizing oRNNs.

2) Theoretical Soundness: The paper provides a solid theoretical foundation for the proposed method and demonstrates its consistency.

3) Performance: The empirical results on benchmark datasets (copy task, MNIST, IMDB) are promising, showing comparable performance to full-precision models. Notably, HadamRNN is the first binary recurrent weight model to handle the copy task over 1000 timesteps.

4) Optimization: The optimized block version of HadamRNN offers improved computational efficiency.


--------------------------------------
After rebuttal:

The authors have addressed my concerns at length and added addiitonal experiments supporting the claims. I am in support of accepting the paper but might not be able to champion it.

### Weaknesses
At a high-level, while I appreciate the work towards making oRNNs work better and efficient, they themselves have quite a few issues including expressivity.

1) Limited Real-World Applicability: While the benchmarks used are common in the literature, they often do not translate well to real-world scenarios. oRNNs, in general, have not seen widespread adoption in practical applications. The paper would benefit from a more thorough discussion of the limitations of oRNNs themselves, and how the proposed method might mitigate or exacerbate these limitations. For example, the inherent constraints on the weight matrices in oRNNs, while beneficial for stability, may limit their ability to model complex dependencies compared to more flexible architectures. A discussion of how the binarization process interacts with these limitations would be valuable.

2) Training Time: The authors mention FastGRNN (Kusupati et al., 2018), which suggests that training oRNN models can be significantly slower (an order of magnitude or more) compared to other methods. It would be beneficial to see a comparison of training times for the proposed HadamRNN models against relevant baselines, including both full-precision and other binarized RNNs, if available. Additionally, a discussion on the stability of training these models would be valuable, including sensitivity to hyperparameter choices such as learning rate and batch size. It would be helpful to see if the training process is more sensitive to these parameters compared to standard RNNs.

3) Lack of Diverse Datasets: The evaluation primarily relies on toy datasets. To strengthen the claims and demonstrate broader applicability, it would be crucial to include more real-world datasets, even if smaller scale, such as those from the GLUE benchmark (e.g., SST-2, QQP) or SQUAD for question answering. The current benchmarks, while useful for initial validation, do not adequately demonstrate the potential of HadamRNN in complex, real-world scenarios. Furthermore, it would be beneficial to see how HadamRNN performs on tasks that require longer-term dependencies, which are often a challenge for RNNs.

### Questions
At this point I am on the border with a leaning towards rejection but the following things might help along with other reviewers comments. 

The paper presents a valuable contribution to the field of oRNNs by introducing a stable and efficient binarization method. However, the lack of real-world evaluation and potential concerns regarding training time and stability hinder its immediate acceptance. I encourage the authors to address these concerns by:

1) Expanding the evaluation to include more diverse and realistic datasets. This would demonstrate the practical value of HadamRNN and provide a more comprehensive assessment of its capabilities.

2) Providing a detailed analysis of training time and stability. This would offer valuable insights into the practical considerations of deploying HadamRNN in real-world applications.

By addressing these points, the authors can significantly strengthen the paper and increase its impact.

### Soundness
3

### Presentation
3

### Contribution
3
