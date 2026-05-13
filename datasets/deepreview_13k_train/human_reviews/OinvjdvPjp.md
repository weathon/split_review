# xVal: A Continuous Number Encoding for Large Language Models

- Decision: Reject
- Scores: 6, 5, 6, 1

## Abstract
Large Language Models have not yet been broadly adapted for the analysis of scientific datasets due in part to the unique difficulties of tokenizing numbers. We propose \xVal, a numerical encoding scheme that represents any real number using just a single token. \xVal represents a given real number by scaling a dedicated embedding vector by the number value. Combined with a modified number-inference approach, this strategy renders the model end-to-end continuous when considered as a map from the numbers of the input string to those of the output string. This leads to an inductive bias that is generally more suitable for applications in scientific domains. We empirically evaluate our proposal on a number of synthetic and real-world datasets. Compared with existing number encoding schemes, we find that \xVal is more token-efficient and demonstrates improved generalization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a simple approach to encoding numerical values as tokenized input to a LLM. Specifically, all numbers $x$ in the input are identified and replaced with the stand-in token '[NUM]', that is then scaled by the value of $x$, i.e., $h(x) := x h(\text{[NUM]})$. This both reduces the number of tokens per number and the vocabulary size, and leads to more efficient training. The paper also demonstrates improved performance at numerical tasks.

### Strengths
The method is simple and easy to understand. It also has some computational benefits. While on simple arithmetic tasks the model performs similarly well to other good approaches (e.g., on 3-5 digit multiplication, P1000 and B1999 encoding schemes can also get near perfect performance), xVal seems to work much better on unstructured, numerical heavy experiments. There are some shortcomings (some of which the authors make a good point of noting), but in general, it seems like a straightforward and effective representation strategy for numerically-dense text.

### Weaknesses
While the continuous nature of the xVal embedding can obviously be an advantage in some domains, I'm not sure how well it would work in general. For example, tasks like summarization, or question answering, where numerical values such as years/dates/account numbers are not meant to be worked with in the sense of arithmetic or other mathematical operations but simply carried about may lose performance. That said, for domain specific applications (like science), this may not be an issue. A hybrid approach may also work (e.g., representing $7.4$ as "+ , 740, e-2, 7.4 * [NUM]").

While the authors touch on the parsing of numerical quantities, the dependence on _accurate_ parsing, especially in messier settings, is a potential limitation.  For example, the regular expression approach may struggle with more complex numerical expressions or with numbers embedded within text in less standard ways. The paper does not discuss how the method would handle cases where the number is not easily isolated or if there are parsing ambiguities. This could be a significant issue in real-world data, where numerical information is not always presented in a clean, easily parsable format. Furthermore, the current multiplicative approach might have difficulty representing very large or very small numbers accurately due to the limited dynamic range of the learned embedding vector and potential issues with numerical stability during training.

### Questions
- I'm not entirely sure why the runtime is so dramatically reduced. Is this due to the reduced length of each input/target and the vocab size? If the latter is a big factor, I'm surprised that what seems like a fairly small additional overhead of the softmax size for everything but FP15 setting would make that big of a difference. 

- I'm curious as to what kind of empirical range the xVal style network has. Is $h(\texttt{[NUM]})$ layer normalized at the end of the network? Is the mapping from $h(\texttt{[NUM]})$ to its numerical value by way of MSE loss minimization linear? I'd imagine that the output range would be restricted in this setup. 

- I'm a bit put off by the dependence on _parsing_ numerical quantities accurately, especially in messier settings. Curious if that posed any difficulties.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces an innovative numerical encoding scheme, designed to efficiently represent any real number using a single token. The encoding leverages a dedicated embedding vector, denoted as `<NUM>`, which is dynamically scaled by the numerical value. This approach significantly optimizes token usage and minimizes the vocabulary footprint.

In addition, the authors complement this encoding scheme with a novel number-inference technique, incorporating a specialized `Number Head`. This `Number Head` enables the model to generate continuous real numbers in an end-to-end manner.

To validate the effectiveness of this proposed methodology, extensive evaluations were conducted on both synthetic and real-world datasets. The results demonstrated consistently comparable or superior performance when compared to prior research in the field.

### Strengths
The strengths of this paper are as follows:

1.  The paper introduces a deceptively simple yet novel approach to real number representation. This design not only minimizes token usage but also significantly reduces vocabulary footprint while preserving the input's value. This simplicity is an attractive feature, emphasizing efficiency without sacrificing performance.
    
2.  The proposed method exhibits outstanding performance, particularly in synthetic datasets used to evaluate multi-digit multiplication and multi-operand binary tree combining. The results indicate that it excels at preserving real number information, outperforming previous approaches in these scenarios.
    
3.  The paper is meticulously organized, presenting the idea in a coherent and transparent manner. It guides the reader through the experimental process, offering a step-by-step validation of the proposed method and effectively highlighting the distinctions from various baseline techniques.
    
4.  One notable advantage of this approach is its adaptability to out-of-distribution inputs. This robustness is inherent in the generation of embeddings, allowing the method to handle cases where certain real numbers are more frequently predicted due to their prevalence or distribution discrepancies between training and testing datasets.

### Weaknesses
This paper, despite its strengths, has some weaknesses:

1.  An issue with the rendering quality on page 2, affecting some figures, diminishes the readability of both the text and data points. The compromised legibility of axis labels and data points could potentially hinder the reader's comprehension and impact the overall impression of the paper.
    
2.  The paper's discussion of implicit normalization and its impact on real number embedding output is not sufficiently clear. The authors fail to provide a lucid explanation of how layer normalization influences the output of real number embeddings and why the normalization into a specific range is performed during preprocessing. Moreover, it remains unclear how these aspects might affect the performance of baseline methods. A more comprehensive and intuitive explanation is required to enhance the paper's accessibility.
    
3.  The experiments conducted in the paper exclusively utilize structured data in JSON format, focusing on scenarios like multi-digit multiplication and multi-operand calculations. While these experiments demonstrate the effectiveness of the proposed approach in these specific contexts, they do not adequately showcase the method's capability to understand real numbers in the broader context of natural language. This limitation may raise questions about the universal applicability and effectiveness of the proposed approach. Expanding the scope of experiments to encompass real-world language contexts would provide a more comprehensive evaluation of its capabilities.

### Questions
1.  Could you please demonstrate how well the proposed method can handle situations where it needs to refer to previously mentioned real numbers in the context, ensuring these numbers remain unaltered? How does this embedding method impact a Language Model's capability to preserve real numbers in the given input?
    
2.  How is the capability of the proposed numerical encoding scheme affected by extremely small or extremely large numbers? Is it able to maintain representation accuracy and robustness in the presence of such numerical extremes?
    
3.  Can you provide an example of a use case where the proposed method demonstrates improved real number understanding capabilities, but the input data is not structured as in JSON, a binary tree, or multi-digit multiplication? This would help illustrate the method's applicability in contexts beyond structured data scenarios.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Large language models rely on predefined tokenizers to process input data. While commonly used tokenizers are constructed for natural language, it is challenging to apply them to numbers. In response, the authors propose a novel method to encode number values for large language models. 

Specifically, at model input, the author proposes to incorporate the numerical value of numbers as a weighted sum of token embedding and position embedding; at model output, the author proposes to construct a separate number head to decide the numerical value and use the original token head to decide whether to use this token. 

The author conducts extensive experiments, which demonstrates the effectiveness of the proposed method.

### Strengths
1. The studied problem is important and may have a big impact. The proposed method is reasonable and novel. 
2. The author conducts empirical evaluations on: a) learning arithmetic; b) temperature forecasting; c) planetary orbit prediction. The proposed method demonstrates consistent performance gain.

### Weaknesses
In experiment setting, the proposed method is only evaluated in the supervised training setting. It is unclear on the impact of the proposed method on pre-training tasks. Specifically, the experiments focus on tasks where the numerical values are directly present in the training data, such as learning arithmetic, temperature forecasting, and planetary orbit prediction. While these tasks demonstrate the method's ability to learn numerical representations, they do not assess its generalization capabilities to unseen numerical values or its effectiveness in a pre-training context where the model is expected to learn more generalizable numerical representations. The evaluation does not explore how the proposed method affects the model's ability to perform tasks that require extrapolation or interpolation of numerical values beyond the training range. Furthermore, the lack of evaluation on standard pre-training tasks limits the understanding of how the proposed numerical encoding interacts with other pre-training objectives.

### Questions
How the training hyper-parameters are configured and why different encodings have different configurations.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed a two-step prediction for floating numerics embedded in the NLG tasks for the LM.

### Strengths
I seldom write this but for this paper it's hard for me to find one.

### Weaknesses
1. Not well motivated. The paper says it's LMs have historically struggled to solve simple arithmetic problems  but somehow many Chain-of-Thoughts paper contradicts the claim. There is no discussion and not literature review enough for this part.

2. The method itself is not very interesting.

3. Evaluation is rough, what are FP15, P10 and so on? No clear elaboration on this.

4. Page 2 is in low-resolution. A not ready draft IMO.

### Questions
I believe at least the paper need to show empirically why the task it difficult.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor
