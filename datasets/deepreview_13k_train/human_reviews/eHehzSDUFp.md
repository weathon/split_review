# Knowledge Entropy Decay during Language Model Pretraining Hinders New Knowledge Acquisition

- Decision: Accept
- Scores: 5, 8, 8, 8

## Abstract
In this work, we investigate how a model's tendency to broadly integrate its parametric knowledge evolves throughout pretraining and how this behavior affects overall performance, particularly in terms of knowledge acquisition and forgetting. 
We introduce the concept of \textit{\entropy}, which quantifies the range of memory sources the model engages with; high \entropy indicates that the model utilizes a wide range of memory sources, while low \entropy suggests reliance on specific sources with greater certainty. Our analysis reveals a consistent decline in \entropy as pretraining advances. We also find that the decline is closely associated with a reduction in the model's ability to acquire and retain knowledge, leading us to conclude that diminishing \entropy (smaller number of active memory sources) impairs the model's knowledge acquisition and retention capabilities.git}}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors identified a phenomenon where language models use less diverse set of value vectors (i.e., the parametric memory store) to learn knowledge. The authors called the distribution "knowledge entropy" and hypothesize that the decrease in knowledge entropy hinders the models' ability to acquire and retain new knowledge. The authors found that the knowledge entropy decreases as pretraining progresses. 

The authors further test the progression of knowledge acquisition (using fictional knowledge probes) and forgetting (using common knowledge datasets) with intervention on the up-projection matrix. The author resusitate the inactive memory vectors by finding the least active $p\%$ of the memory vectors and multiply the up-projection matrix by the ratio $q$ at the corresponding index. The authors show that this reduce forgetting and increase retention of new knowledge (I have questions regarding this -- see the question section).

### Strengths
This paper investigates an important problem of knowledge acquisition and retention in LLMs. The angle is simple, clear, and easy to validate. The idea is not particularly high on the originality end but the identified "variable" (i.e., the knowledge entropy) has not been used to understand forgetting/retention as far as I know.

### Weaknesses
The main concern is it's unclear how causal the knowledge entropy is to the phenomenon of knowledge forgetting/retention. The paper provided mostly correlational evidence. Please see the Questions section for more concrete critique and suggestions.

**Presentation Issues**

Quite a bit of notation overloading:
1. c is used for the memory coefficient in equation 2 and used again in section 4.1 L303 to represent knowledge.
2. $m$ is used for index in equation 2 and then as multiplier in algorithm 1
L320: missing space between sentences.

### Questions
In L209, the negative value is often understood to remove/erase the information from the residual stream. If this flexibility is removed from the model, it could affect the model's plasticity. It would be useful to see a more flexible gating function. The entropy can still be calculated using the absolute values of the coefficients (and does not need to change the model arch and training).

What does section 3.4 do to support the use of knowledge entropy? I understand the concept of attention entropy and next token entropy but how does that connect to the choice of using knowledge entropy? In fact, if all these entropy measures decrease over time, how can we justify that knowledge entropy is the main reason for the degraded plasticity even if it shows high correlation? Section 4.3 provides interventional evidence but similar intervention should be done with, say, attention entropy to ensure this is not the source for the lowered plasticity. I.e., if making attention entropy less peaky also increase retention and mitigates forgetting, then the role of knowledge entropy is not unique as other statistics reflect the same phenomenon. Would be nice to see more interventional evidence showing that knowledge entropy is the main contributor to the plasticity issue.

Figure 5 (b): seems that downstream performance decreases as the $q$ value gets larger, which is the opposite of knowledge retention? And the knowledge probing result in the same plot doesn't show improvement over lower $q$ values. Am I missing something or does it show a different trend than Figure 5 (a)?

I'm happy to increase my scores if the above questions can be addressed.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work introduces the concept of "knowledge entropy" to analyze how language models integrate their stored knowledge throughout the pretraining process. By viewing feed-forward layers as key-value memory systems, the researchers measure how broadly or narrowly models access their stored knowledge by calculating the entropy of memory coefficients. Their key finding is that as pretraining progresses, models exhibit decreasing knowledge entropy, meaning they tend to rely on a narrower set of memory vectors rather than broadly integrating knowledge from many sources. This narrowing correlates strongly with decreased ability to acquire new knowledge and retain existing knowledge during continual learning, an interesting empirical finding.

### Strengths
The concept of "knowledge entropy" introduced in this paper is novel and very interesting. (1) Entropy based metrics have been used in previous works before. (2) Recent works have gradually built the view of feed-forward layers as key-value memory. This paper has a refreshed view, combining these 2 insights to give a new metric. 

The "resuscitation" method, by manipulating parameters, presents somewhat a direct test for the authors' main claim that decreased knowlege entropy gives rise to decreased ability to learn new things.

### Weaknesses
This work only tested on OLMo models (1B and 7B), as acknowledged by authors. The authors state their reasons for this as due to the fact that OLMo provide intermediate checkpoints. 

However the Pythia models, too, offer intermediate checkpoints. If time permits, the authors should endeavor to check their results on these models too, in order to ascertain the generality of their claims and whether it holds beyond a single model family. 

It would also be useful if the authors provide some discussion regarding mechanisms behind their main finding (knowledge entropy correlates with decreased ability to acquire new knowledge). It does not need to be theorem based, which is a difficult endeavor. Empirical findings would help, to delve at least a bit deeper into this phenomenon and why it might occur.

### Questions
1. Why do you think that knowledge entropy correlates with decreased ability to acquire new knowledge? 

2. Is the resuscitation method intended solely as a test for your main finding, or do you also envision a path in which this could practically be useful for increasing plasticity of models?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper investigates how knowledge acquisition and forgetting evolves through an LLM's pretraining. Building on the work of Chang et al 2024 and Geva et al 2021 and 2022, the authors introduce a concept of knowledge entropy and show that low entropy, which corresponds to poor knowledge acquisition and high forgetting rate, occurs in late stages of pretraining while high entropy occurs for initial stages of pretraining.

### Strengths
This work exposes an important feature of pretraining and contributes valuable insights to LLM pretraining.  
While the definition of knowledge entropy to this reviewer is not completely clear, it is an important feature of it that it patterns with other notions of entropy in models like attention entropy or next token prediction entropy.   The work on knowledge acquisition and forgetting is potentially very important for how we view model training.


The empirical results are solid and convincing to this reviewer.

### Weaknesses
This paper has the potential to make substantial contributions to the NLP and ML communities.  But I believe it still could benefit from further work.

The talk of broad and particular memory vectors in the introduction is a bit unclear.

In calculating entropy, the authors assume the feed forward network has the form
FFN(x) = f(x · K^T ) · V
but this leaves out important bias terms that might perhaps affect the calculations.  Can the authors say more about this?


There are some important connections with Chang et al 2024 that need to be brought out more.  As it stands, it seems as though much of the heavy lifting is done in Chang et al, and this paper provides an incremental improvement to that paper.  There needs to be a discussion of how this paper goes beyond the previous one.  

Also it is important to not oversell the information contained in the so called memory vectors.  In particular, given the experiments with human interpreters given the strings that affect these memory vectors the most,  what we get are suggestive interpretations of what's stored, that is suggestive to those particular human interpreters.  As far as I know Chang et al shows mostly  it's not clear that the model can make use of them in the way they are interpreted.

While it's pretty clear intuitively what attention entropy or next token prediction entropy are, it's less clear at least to this reviewer what the intuition is behind defining entropy in terms of the coefficients of the outputs of a given FFN layer in the model.   How does the knowledge entropy so defined link up with the suggestion that "models in the later stage of pretraining tends to engage with a narrower
range of memories, relying more heavily on specific memory vectors rather than accessing and integrating
knowledge from a broader range of memories"?

Another element that needs a bit more work is the discussion of knowledge acquisition and forgetting.  This relies on work from Chang et al. but to be more self-contained the authors could explain in a bit more detail what the probes are doing (and why, for instance, 15 different probes?), or rather summarize Chang et al's contributions more clearly with respect to the contributions of the present work.

That part as it stands leaves this reader wanting more information.  For instance, what is the target span for the probes?  Also is \theta_{pt} unique? Is there only one such check point and what about \theta_{cl}?  Is \theta_{cl} when the continual learning stops, if it does, or what?  Is  \theta_{cl} then the model after pre training?   There is more material in the appendix on this but it would help the reader's understanding of this important concept of knowledge acquisition and knowledge loss  to move some of that discussion into the body of the paper.

Some minor stylistic corrections that will render the paper more readable:

Works ---> work   (`work' is still a mass known in English, as far as I know)
coefficient of j-th token  ---> coefficient of the  j-th token

into probability distribution --> into a probability distribution

We also experiment that the trend persists ---> We also show experimentally that the trend persists

we inject FICTIONAL KNOWLEDGE dataset  ---> we inject elements of the FICTIONAL KNOWLEDGE dataset??

of target span  ---> of the target span

Equation and detailed explanation is
presented  ---> please fix the English

Hoyeon Chang, Jinho Park, Seonghyeon Ye, Sohee Yang, Youngkyung Seo, Du-Seong Chang, and Minjoon
Seo. How do large language models acquire factual knowledge during pretraining? arXiv preprint
arXiv:2406.11813, 2024.

### Questions
Please address the questions about bias, and also about how knowledge entropy links to intuitions about types of memories.  Finally please answer the questions about probes and knowledge acquisition.
Could you more clearly articulate how this paper builds on chang et al with respect to the part on knoweldge acquisition and forgetting?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces knowledge entropy as a novel concept for the quantification of model representation across Large Language Models. The authors show that as the training of a large model progresses, the knowledge tends to concentrate in a smaller set of "memory vectors", making the process of knowledge acquisition difficult (decrease in plasticity), and the model more prone to forgetting prior knowledge as memory vectors are forced to be constantly rewritten. Experimental results show that it is indeed the case that models in the later stages of their training are more resilient to learning new knowledge, and tend to easily forget the knowledge that they already have. In addition, by resuscitating the inactive vectors, the authors force a later-stage model to ameliorate both the aforementioned concerns in the continual learning process.

Overall, I think this is a good paper with interesting results that can have further applications for the community. Some concerns and questions still remain as outlined below, but I am willing to increase my score once they are addressed.

### Strengths
- The proposed framework of categorizing knowledge retention in terms of the model's knowledge entropy is interesting albeit somewhat expected as it is generally understood that moving away from established weight matrices becomes more difficult as the training progresses.
- The concept of entropy in this case is both well-defined and intuitive, essentially showing how variant the coefficients are with respect to each input token given an instance.
- The experimental results confirm the theoretical hypothesis, strongly indicating that knowledge entropy is associated with both learning and forgetting.

### Weaknesses
 - The usage of the term "entropy" in this case can be confusing in my opinion. Usually, this term implies some form of "surprise" with respect to information. However, in this case, it seems to refer to the idea of source broadness. It is not clear that the proposed definition of knowledge entropy aligns with the traditional information theoretic interpretation, which could lead to misinterpretations of the results. A more thorough justification of the use of the term "entropy" in this context is needed, perhaps by relating it to existing concepts in information theory or by providing a clear explanation of the conceptual differences.
- I think this is a paper that could benefit greatly from further evaluation with respect to knowledge entropy. Although it is expected that the same behavior is observed across models, I would like to know if different architectures affect the observed behavior and if different training time design choices can regulate the knowledge entropy on a case-by-case basis. Specifically, it would be valuable to investigate if different activation functions, layer normalization techniques, or optimization algorithms can influence the observed trends in knowledge entropy. Furthermore, the effect of varying the dataset size and composition on knowledge entropy should be explored. Such an analysis would help to establish the robustness and generalizability of the proposed concept.
- Further discussion is required regarding the correspondence of knowledge entropy and forgetting. Rather than being a direct consequence of knowledge entropy, can it be the case that the reason behind sharper declines in knowledge retention is due to the model's richer knowledge representation between concepts at later stages of the training and thus being more prone to knowledge loss when small changes are made? More specifically, forgetting at a higher rate at later stages can be expected simply due to having more knowledge encoded in comparison to having very little knowledge in earlier stages. The paper should explore alternative explanations for the observed forgetting behavior, such as the potential for catastrophic interference due to overlapping representations or the effect of parameter saturation. A more rigorous analysis is needed to establish a causal link between knowledge entropy and forgetting, rather than just a correlation.
- Minor grammatical errors that can be fixed in the camera-ready version.
- I believe that Algorithm 1 can be rewritten to better relay the information contained. Namely, by giving a better explanation of each operation (especially with respect to $t$). The current description of Algorithm 1 lacks clarity, particularly regarding the role of the parameter $t$ and its impact on the resuscitation process. A more detailed explanation of the mathematical operations and their implications for the model's internal representations is needed.

### Questions
- Given that consistent behavior is observed across all layers, do you think we can use only a subset of layers to determine the model's proneness to learning new knowledge? For example, only focusing on layers that mainly encode semantic knowledge as shown in the literature. 
- Related to the question above, is the same trend observed across different forms of knowledge and is there a difference between various knowledge forms (syntactic knowledge versus semantic knowledge for example)? 
- Given the minor negative effects of resuscitation of inactive vectors, do you think this is a viable method for adaptation in continual learning frameworks in generals to minimize forgetting and increasing knowledge acquisition? More specifically, what negative effects can this artificial resuscitation have?
- In Figure 5(b), what is the reason behind the decrease in the downstream task performance while a drastic decrease in forgetting is also observed? Shouldn't a low forgetting rate lead to better general-purpose performance?

### Soundness
3

### Presentation
3

### Contribution
3
