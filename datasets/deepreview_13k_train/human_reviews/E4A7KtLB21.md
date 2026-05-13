# Unbiased Attribution with Intrinsic Information

- Decision: Reject
- Scores: 3, 5, 5, 3

## Abstract
The importance of attribution algorithms in the AI field lies in enhancing model transparency, diagnosing and improving models, ensuring fairness, and increasing user understanding. Gradient-based attribution methods have become the most critical because of their high computational efficiency, continuity, wide applicability, and flexibility. However, current gradient-based attribution algorithms require the introduction of additional class information to interpret model decisions, which can lead to issues of information ignorance and extra information. Information ignorance can obscure important features relevant to the current model decision, while extra information introduces irrelevant data that can cause feature leakage in the attribution process. To address these issues, we propose the Attribution with Intrinsic Information (AII) algorithm, which analyzes model decisions without the need for specified class information. Additionally, to better evaluate the potential of current attribution algorithms, we introduce the metrics of insertion confusion and deletion confusion alongside existing mainstream metrics. To continuously advance research in the field of explainable AI (XAI), our algorithm is open-sourced at https://anonymous.4open.science/r/AII-787D/.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a novel feature attribution method, Attribution with Intrinsic Information (AII), designed to address challenges in current feature attribution algorithms, specifically regarding “ignored information” and “extra information.” AII accumulates gradients across the prediction vector, which may allow attribution map to capture features contributing to competing classes. Additionally, the paper proposes a a new evaluation metric that addresses a problem of the existing insertion and deletion metric. The effectiveness of AII is demonstrated through several experiments on image classification.

### Strengths
1. This paper presents a novel method for feature attribution.

2. The experiments include a variety of baseline feature attribution methods.

3. The code is available.

### Weaknesses
1. The key concepts, information ignorance and extra information, are not well-defined in the paper. Instead, these concepts are almost completely illustrated through examples in Figure 1 and Figure 2. While I appreciate the illustrative examples, it is unclear what exactly do they mean in a general setup. Specifically, it is not clear how these concepts relate to the underlying mathematical formulation of feature attribution methods. For instance, how can one quantify the amount of information ignorance or extra information present in a given attribution map? Without a formal definition, it's difficult to assess the validity of the claims made about these concepts.

2. The proposed method is described within half a page in Section 3.4. And it's unclear how does the proposed method mitigate the claimed problems (in fact, this may not be possible without clear definitions of the two problems). The description lacks sufficient detail to understand the precise mechanism by which the gradient accumulation across the prediction vector leads to the desired properties. It is also unclear how the method avoids the pitfalls of other gradient-based methods, especially given that it still relies on gradients. A more rigorous mathematical treatment of the proposed method and its connection to the identified problems is needed.

3. Some claims do not seem accurate. For example, in line 157-158, I do not understand why "the loss function L(f (x), y) only contains the class information of y" since for cross-entropy loss, the loss also depends on the output logits for other classes. While the loss is indeed minimized with respect to the target class, it is not accurate to say that the loss function only contains information about the target class. The gradients with respect to the logits of non-target classes are also non-zero and contribute to the overall optimization process. This mischaracterization of the loss function undermines the subsequent arguments.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces an approach named AII to address biased attributions given by existing approaches. The sources of biased attribution are categorized into information ignorance and recognition of irrelevant features. This work mainly proposes two concrete improvements: (1) more advanced feature removal through entropy maximization, which could be used to develop an unbiased evaluation metric, and (2) considering the information of all classes during attribution, which is used in AII.

### Strengths
The phenomenon of two attribution biases, including omission of important features and incorrect identification of irrelevant features as significant, is explained well with clear examples.

The extensive experiments show the great effectiveness of the proposed approach, primarily due to the high insertion score. This could be potentially explained from the provided examples as the explanations given by AII appear to be less noisy and concentrate more on important areas.

### Weaknesses
I am unsure about the settings of the example in Fig.2. This example tries to show that other algorithms wrongly capture the irrelevant square region. From the understanding of humans, the square region is indeed irrelevant. But the attribution methods are designed to explain model behaviours instead of human understanding, and the model might be erroneous and actually use that region for classification. That is, the example might also need to prove that, the model does not leverage that square region. Maybe it could be done by control experiments.

I like the interesting case presented in Fig.1, where the confidence is low due to ambiguity. However, it seems those cases could not be captured by the metrics used in experiments, because the calculating of scores does not involve reconstructing the exact same low-confidence prediction. Also it might be helpful to replace Fig. 6 or 7 with an example in such scenario.

I understand that the existing feature removal needs to be improved, but I don’t have a good intuition about why entropy maximization would help. Maybe more intuition could be added around lines 300-304.

I am concerned that the AII algorithm does not help explain less ambiguous figures such as Fig.3. And, for instance, in the MNIST data, it seems the large majority of figures are actually not that ambiguous.

### Questions
The observation in Fig.3 is interesting, and I wonder if this is a feature of the model or a “bug” in the attribution approach that needs to be addressed. If the same thing happens in the example of Fig.1, and considering the proposed AII algorithm is essentially summing all those attributions (maps), the attribution in Fig.1 should only highlight the dog area?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focused on feature-level data attribution and pointed out two possible issue in traditional gradient-based methods: Information Ignorance and Extra Information. The paper proposed Attribution with Intrinsic Information (AII), a new feature attribution method which accumulated the gradients for the sum of log predicted probabilities for all classes. Furthermore, the paper also proposed evaluation methods

### Strengths
- The paper did some evaluation to show that the method proposed (AII) outperformed other traditional methods.
- The proposed method empirically resolve the problem spotted by the paper (i.e., Information Ignorance and Extra Information)

### Weaknesses
 - There should be a more intuitive and clear-to-understand illustration for Information Ignorance, Extra Information, what does the traditional algorithms care about and what does AII care about. It could be a diagram or a Venn diagram.
- It still hard to understand why AII could resolve the Extra Information (and the cause of extra information).
- More examples showing the problems (Information Ignorance, Extra Information) are resolved will be helpful.
- Some small typos
  - Table 2 caption: U-INS, U-DEL -> F-INS, F-DEL
- The experiment is carried out on image classification with some very popular dataset and models, it could be biased.

### Questions
- What’s the difference between high-confidence and low-confidence? Like high-confidence cover 90% and low-confidence cover 10%? Or it’s a 50-50 separate.
- Is there any possibility that the issues could be presented by math terms. Current illustration is clear (emperically) but not well-defined by anything other than plain text.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a new method to perform feature attribution called AII. They also suggest an approach (CFA) to find the correct null values for an image which would more closely emulate removal of superpixels from an image relative to a human. The AII algorithm they claim mitigates two issues other attribution methods have namely, feature ignorance and extra information.

### Strengths
+ Interesting setting
+ Reasonably thorough experiments

### Weaknesses
 - Poor presentation
- No details given in the figure captions (1-5) of what models were used for the task and in some cases also the attribution method is missing. The text referring to them also does not contain this information.
- Presented solutions such as CFA are expensive
- Inconsistent and sometimes erroneous notation
- AII algorithm description extremely curt which is their main contribution
- No discussion or comparison with contrastive/counterfactual explanation methods

The way the extra information part is written is confusing. The writing implies that somehow the including the class information during attribution is the extra information. What they mean by extra information only becomes clear when the discuss Figure 2, where it is more a statement about the input space and superfluous features selected therein.

AII algorithm description is quite short given that it is one of their main contributions. There is no discussion on why the 2 issues of extra information and information ignorance are mitigated by their approach. The approach essentially takes an average gradient over all class predictions, which also seems to have limited innovation (given that other averaging approaches such as Integrated Gradients etc. although somewhat different already exist).

Also the AII algorithm uses an adversarial attack strategy which is reminiscent of contrastive/counterfactual explanation methods (viz. contrastive explanations method (CEM), etc.). But no discussion is provided relative to those.

The CFA problem posed in Equation 2 is a hard optimization problem. To solve it for each image to find the null pixel values seems quite computationally intensive.

They consider just turning pixels black as the only solution for feature removal. However, that is not true. The idea in most of those methods is to insert a null value (also done in SHAP) which may be black pixels but could also be another value say average pixel value across the image or other images in the dataset. This phenomenon is not a new insight. 

Equation 2, the sum uses index i but the term has j in it. $x_1, ..., x_n$ are not defined. Although I presume they imply pixel values.

$x^t$ I presume implies the $t^{th}$ image, but it is sampled from a univariate uniform distribution. If they are pixels then a subscript has become a superscript.

Experiments are reasonably thorough given that they compare against a bunch of different methods also using the setup of previous studies. However, I would have also liked to see timing results as the optimizations they propose for CFA and AII seem to be much more expensive than the attribution baselines.

Minor comment:
> "The larger the
attribution result, the more important that dimension is for the model’s decision."
I think this statement has to be qualified by saying larger the *absolute value* of the attribution ... Because a larger negative value also indicates an important feature

### Questions
The way the extra information part is written is confusing. The writing implies that somehow the including the class information during attribution is the extra information. What they mean by extra information only becomes clear when the discuss Figure 2, where it is more a statement about the input space and superfluous features selected therein.

AII algorithm description is quite short given that it is one of their main contributions. There is no discussion on why the 2 issues of extra information and information ignorance are mitigated by their approach. The approach essentially takes an average gradient over all class predictions, which also seems to have limited innovation (given that other averaging approaches such as Integrated Gradients etc. although somewhat different already exist).

Also the AII algorithm uses an adversarial attack strategy which is reminiscent of contrastive/counterfactual explanation methods (viz. contrastive explanations method (CEM), etc.). But no discussion is provided relative to those.

The CFA problem posed in Equation 2 is a hard optimization problem. To solve it for each image to find the null pixel values seems quite computationally intensive.

They consider just turning pixels black as the only solution for feature removal. However, that is not true. The idea in most of those methods is to insert a null value (also done in SHAP) which may be black pixels but could also be another value say average pixel value across the image or other images in the dataset. This phenomenon is not a new insight. 

Equation 2, the sum uses index i but the term has j in it. $x_1, ..., x_n$ are not defined. Although I presume they imply pixel values.

$x^t$ I presume implies the $t^{th}$ image, but it is sampled from a univariate uniform distribution. If they are pixels then a subscript has become a superscript.

Experiments are reasonably thorough given that they compare against a bunch of different methods also using the setup of previous studies. However, I would have also liked to see timing results as the optimizations they propose for CFA and AII seem to be much more expensive than the attribution baselines.

Minor comment:
> "The larger the
attribution result, the more important that dimension is for the model’s decision."
I think this statement has to be qualified by saying larger the *absolute value* of the attribution ... Because a larger negative value also indicates an important feature


Overall, the paper requires significant rewriting in my opinion and is not currently ready for primetime.

### Soundness
3

### Presentation
1

### Contribution
2
