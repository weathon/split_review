# Intrinsic Evaluation of Unlearning Using Parametric Knowledge Traces

- Decision: Reject
- Scores: 6, 5, 6, 5, 6, 3, 8

## Abstract
The task of ``unlearning'' certain concepts in large language models (LLMs) has attracted immense attention recently, due to its importance in mitigating undesirable model behaviours, such as the generation of harmful, private, or incorrect information. Current protocols to evaluate unlearning methods largely rely on behavioral tests, without monitoring the presence of unlearned knowledge within the model's parameters. This residual knowledge can be adversarially exploited to recover the erased information post-unlearning.
We argue that unlearning should also be evaluated internally, by considering changes in the parametric knowledge traces of the unlearned concepts. 
To this end, we propose a general evaluation methodology that leverages vocabulary projections to inspect concepts encoded in model parameters. We use this approach to localize ``concept vectors'' --- parameter vectors that encode concrete concepts --- and construct \dataset{}, a benchmark dataset containing hundreds of common concepts and their parametric knowledge traces within two open-source LLMs.
Evaluation on \dataset{} shows that existing unlearning methods minimally impact concept vectors and mostly suppress them during inference, while directly ablating these vectors demonstrably removes the associated knowledge and significantly reduces the model's susceptibility to adversarial manipulation.
Our results highlight limitations in behavioral-based unlearning evaluations and call for future work to include parameter-based evaluations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes an evaluation metric of LLM unlearning using vocabulary projections and concept vectors. The authors construct a benchmark dataset based on this, named CONCEPTVECTORS. In the paper, they conducted experiments to study the performance of various unlearning methods using this benchmark.

### Strengths
The paper provides a novel aspect to evaluate the LLM unlearning, using the encoded concept vectors. This leads to a more internal and intrinsic way to unlearn certain information. In this paper, they verified that the existing methods mostly only suppress the information, instead of erasing them. Then uses both intrinsic evaluation and behavioral tests to valid the idea. Combined with the jailbreak attacks, the experiments greatly improve the quality and significance of their work.

### Weaknesses
First, a relatively minor weakness is on the presentation of the paper. The discussion about the concepts is clear. However for the discussion of constructing the dataset. There might be too much detailed discussion about validations of manual quality checking by humans, it could possibly be moved into the Appendix. Besides that, there are many hyperparameters in the entire experiment setup and dataset construction. It would be better to provide a more systematic exploration to study their effects, in order to make the results and the contribution more robust. Moreover, the results seem to be limited to the two chosen models (LLaMA and OLMo).

### Questions
The concept vectors are based on the two models LLaMA and OLMo. For unlearning using other models, is there a way to directly apply the benchmark CONCEPTVECTORS to use on other model architecture?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a benchmark for unlearning methods to test residual intrinsic knowledge (i.e. stored in model parameters) and evaluate if respective unlearning methods _causally_ erase the concepts to be unlearned. This benchmark is motivated that current unlearning methods only unlearn in a shallow way (i.e. behavior) while the model continues to possess conceptual knowledge that can be adversarially retrieved (e.g. by using an adversarial suffix, advanced prompting, etc.). Towards this, they introduce a method, _Needle_, to identify "concept vectors" within transformer models' MLP layers -- that encode the said concepts. Using this method, this work introduces a metric to enumerate how much a given unlearning technique is _causally_ erasing the underlying knowledge. The paper presents experimental results that [i] include assessing various unlearning methods with their _intrinsic_ metric + targeted unlearning behavioral metrics i.e.  (Table 3) and [ii] the impact of adversarial attacks to extract the underlying unlearned knowledge on various respective unlearning methods including their own introduced method _Needle_ (Figure 3).

### Strengths
- The draft is well-written, presentable, and is read easily.
- The results from (ii) [from summary] are strong. The introduced method affects untargeted QA less than baselines when prompted adversarially (Figure 3).

### Weaknesses
The main weakness that makes the work uncompelling is that it breaks the hypothesis that "concept vectors" exist by definition. Unlearning at its core is supposed to return a model that operates like it has never seen a forget set which is primarily _behavioral change_ (while preserving the utility of the model as much as possible). I agree with the authors that this is not causal since information is still retrievable through advanced prompting or adversarial attacks, alluding to the fact that residual knowledge is retained. But given the fact that Needle (concept vector perturbation) itself doesn't induce such behavior change (getting 3x worse bleu score than the simple gradient ascent in Table 3) points the concept vectors don't work as hypothesized/defined and are thus not suitable for evaluating/benchmarking unlearning. I would argue that claiming to measure _causal_ unlearning, (and not just behavior) is even more strict and doesn't make sense if it's not backed up by behavior unlearning ( in fact, it's not causal at all in such case). 

This gap in performance might be due to the violation of the unsaid (and/or untested) assumption that information or concepts reside in a concentrated manner in a few selected params and are not diffused across params globally. It would be great to have this assumption experimentally validated. In other words, intrinsic should at least rank order behavioral scores which it doesn't.

Other than that, the reported results include manually reviewing/handpicking concept vectors -- which would be not scalable to benchmark unlearning methods, making it impractical. 

The adversarial attacks used for experiments (Section 5) do not include the strongest attack such as GCG [1].

It would be better to see the model evaluation harness scores [2] than just untargeted QA to see the degree to which Needle affects the underlying model utilities. Also, it would be better to see the performance (behavior vs model utility, untargeted QA) by individual adversarial methods than aggregated over multiple methods like in Figure 3.

The current set of experiments doesn't dig deeper to be convincing in my opinion. For example, if we look at the _concept vectors_ from a model trained without _forget set_ (samples provided for unlearning) i.e. a control model and keep other training data/scheduling as is (i.e. in controlled settings), we can compare that to validate if the knowledge is in fact concentrated in said vectors. This is computationally difficult for larger models, but certainly possible for smaller GPT-2 level models as done in [3]. 

---
[1] Andy Zou, Zifan Wang, J. Zico Kolter, and Matt Fredrikson. Universal and Transferable Adversarial Attacks on Aligned Language Models.

[2] Gao, L., et al, "A framework for few-shot language model evaluation," 2024, https://github.com/EleutherAI/lm-evaluation-harness

[3] https://physics.allen-zhu.com/

### Questions
1. In line 202, "Note that in both settings there is no need for gold answers or references, as our goal is to evaluate the effect of unlearning on the model’s outputs" -- why don't we need gold answers?
2. In Step 3, line 207, how do you ensure that these concept vectors aren't cohesively tied up with other concepts? Like parameters are compression of training data -- so they would likely to be not isolated to selected concepts.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The submission presents a new benchmark for Machine Unlearning, with a specific focus on ensuring data is removed from the model weights, not just from the model's behavior. The benchmark finds concepts represented in model weights, synthetically generates questions about that concept and retrieves Wikipedia articles about the concept, then validates the concept vectors ablating them and observing the impacts on the collected data. Concept vectors which have large but targeted impact on the concept are taken as unlearning targets. The benchmark then evaluates unlearning algorithms based on whether they remove the concept vector (based on change in predicted tokens), as well as standard behavioral tests.

### Strengths
1.	Submission targets an important and relevant question: do unlearning algorithms actually remove the information they claim to?
2.	Submission is well-written and results are presented well
3.	Provides interesting analysis on the effect of jailbreak attacks on model internals post-unlearning.
4.	It was interesting to use MEMIT as an unlearning method to remove internal concept representations.

### Weaknesses
1.	The authors claim that "This work presents the first benchmark for internal evaluation of unlearning methods." However, there is at least one benchmark [1] that trains linear probes on the activations of the models, trying to predict answers to held-out questions based on the model's internal representations. This submission cites [1] in Section 6 but does not evaluate against the method from [1] that address some of the concerns raised about other unlearning methods not removing internal concept representations. 
2.	Submission uses the MLP basis for selecting concept vectors, which does not seem ideal for finding concept vectors, as it restricts concept vectors to the neuron basis and there is a consistent view in the mechanistic interpretability literature that neurons are polysemantic. If the concept vectors are polysemantic, then it is possible that unlearning algorithms may avoid removing them to prevent losses in other tasks
3.	There are a few of components in the dataset generation process that required manual input that seemed a bit vague in definition:
a) In 3.1 Step 1: “Last, we (authors) manually review the top-scoring vectors and select those exhibiting a clear pattern corresponding to a concrete and specific concept.” – what is the definition of a “clear pattern” and a “concrete and specific concept”?
b) In 3.3: “we manually verify that the questions are about the given concept and that they are simple and reasonable.” 
4.	Specific tokens may not be the best way of describing a concept because with individual tokens it can sometimes be ambiguous how they are used contextually.
5.	It is unclear what quality-control measures when generating the behavioral tests. I think this stage, where concepts are generalized from single tokens to entire questions or paragraphs, is a place where things could go wrong.
6.	At a higher level, it is unclear how deriving concepts directly from the model causes differences from pre-selecting concepts. It seems plausible that taking concepts directly from model parameters creates concepts that don't align with what a human would define as the concept. There may be other ways in which these model-derived concepts are subtly different from a concept that a human would request to be unlearned. This is fairly speculative, however. The authors do seem to acknowledge limitations in deriving concepts directly from the model.
7.	Results are generally not as convincing with OLMo as Llama-2 (for example Figure 4). Submissions would benefit from evaluating another model. 
8.	Use of Needle as an 'oracle' is called into question in Figure 3, since for OLMo Needle performs very similarly to other methods, and appears to even be outperformed by MEMIT. This could indicate issues with the methodology (e.g. for validating concept vectors). 

[1] Li, Nathaniel, et al. "The wmdp benchmark: Measuring and reducing malicious use with unlearning." arXiv preprint arXiv:2403.03218 (2024).

### Questions
1.	Suggestion: reword claims on novelty of internal evaluation for unlearning.
2.	Question: can you explain your reasoning for extracting potential concept vectors in this manner as opposed to others?
3.	Question: could you address some of the concerns around the selection of concept vectors, especially their utility and cases such as the McDonald's concept?
4.	Question: can you explain why results for Llama and OLMo are different?
5.	Question: can you explain the poor performance of Needle in Figure 3 (and 5 and 6)?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a dataset of vectors associated with different concepts, which can be used to test whether an LLM has a knowledge about a topic. This is particularly relevant for unlearning, where these vectors can be considered an audit tool to check whether the knowledge has been truly removed or just suppressed.

The vectors are obtained by selecting some columns in the output of some MLP layer, based on the average logit score of the columns (after multiplying by the output embedding). The scores are checked with GPT-4 and manually.

Concept vectors are then used to evaluate how effective some common unlearning methods are, and it is proposed a new method, Needle, that perturbs the concept vector associated with the concept to be unlearned. The conclusion is that current unlearning methods obfuscate the knowledge rather than removing it. Needle turns out to be robust to adversarial attack.

### Strengths
Concept vectors might be useful to locate knowledge associated with a specific topic and used as an audit tool to check whether unlearning happened successfully. More generally, locating specific knowledge might help in interpreting the behavior of LLMs.

### Weaknesses
- The score description should be more precise. For example it’s not super clear how to judge whether a single token is relevant to a topic. A single token can be relevant to multiple topics.
- It’s not clear how the vectors are selected. After the score is computed, are the vectors selected for a fixed layer? Does the layer depend on the concept?
- The Needle unlearning baseline is similar to RepNoise and RMU, so an additional comparison with these two methods would be useful. They seem to be robust to jailbreak attacks too.
- It’d be good to include an evaluation of suffix based adversarial attacks, like GCG
- It’d be good to find concept vectors for a bigger set of models

### Questions
- There exist methods that try to locate concepts by looking at the internal activations (activation addition, representation engineering etc). How does your method compare to those?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a new benchmark called ConceptVectors, for evaluating unlearning in large language models by tracking parametric knowledge traces. The key motivation for the work is that current unlearning evaluations rely primarily on behavioral tests, without considering whether the knowledge is actually erased from the model's parameters. The authors propose a methodology to identify "concept vectors" - specific parameter vectors that encode concrete concepts - and construct a benchmark containing hundreds of common concepts across two open-source LLMs. They found that existing unlearning methods mostly suppress concept knowledge during inference rather than truly removing it, making models susceptible to adversarial attacks that can recover the "unlearned" information. In contrast, directly ablating concept vectors proves more effective at genuine knowledge removal and improves robustness against jailbreaking attempts.

### Strengths
The paper builds an excellent automated pipeline to automatically discover directions in parameter space that encodes the knowledge about any concept. 

Their evaluations are very thorough


The paper is very well presented

### Weaknesses
While the premise of concept vectors is very intriguing, the main qualitative evidence that concept vectors encode the knowledge of a concept in the models is not very clear. The numbers indicate that concept vectors are not really erasing the knowledge (high BLEU and Rouge scores). 

It is slightly unclear what the concept vectors are really encoding? Is it the knowledge exclusively or something more higher level like "everything" about the concept including grammar and comprehension

### Questions
The text for Table 3 is very confusing. In section 4.3: "While gradient-based and preference-based optimization methods substantially restrict models from generating information about the concept (with Target QA and text completion scores < 0.25)" - so the BLEU scores <0.25 is considered that the model is behaviorally showing unlearning. But Needle has much higher BLEU scores but the authors claim that as unlearning too? ("while demonstrating prominent effect on the model’s outputs (50% − 70% decrease in QA performance)"). This is confusing. I could be missing something here - would love some clarity on this


The original space to search for concept vectors was very large as noted by authors and they propose some clever ways to filter this search space. Primarily "we sort the column vectors based on the average logit value in the projection to the vocabulary, Intuitively, this score indicates how strongly the vector promotes a specific concept". And they discard some non-important MLP layers to continue their search. What happens if you search in the discarded MLP space? It doesn't sound intuitive at all - but this could be a good experiment to show for strengthening the intuition claims.


The entire pipeline for finding concept vectors is very well designed and automated. I am curious as to how much time it takes for a new user to run this pipeline for erasing or analyzing a concept of their choice? 

Previous unlearning methods like RMU (https://proceedings.mlr.press/v235/li24bc.html) show their efficiency in parameter space by training probes at each layer and showing that there is no knowledge traces. What are the authors views on this? Is this doing something similar to looking through lenses? 


Some evaluation questions:
1. How does the Needle method work when prompted with multiple choice questions? For instance, if I remove Harry Potter and test MCQ accuracy on this dataset? How does the generation look for this dataset? Lynch et al found that prompting with context is a good attack method in some unlearning methods. This could be interesting to look at

2. Why is the unlearnt model (NEEDLE) outputting repeated patterns? (appendix Table 8.) Does this mean that concept vectors also encode grammar in the models? Not just the concept? It almost feels like NEEDLE is basically finding neurons responsible for concept generation and simply ablating it is also removing the "speaking ability". So maybe that says something about the model's mechanisms? I would like to know what the authors think about this?


I am majorly concerned about the Table. 3 results and would like more clarity on the evaluations what are the BLEU scores being calculated against. Happy to reconsider my rating after this clarity

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper identifies an explainability technique to better measure unlearning.

### Strengths
1. The notion of a concept vector as it relates to unlearning is novel to my knowledge.
2. The writing is clear, well formatted, and fluid.
3. The explanatory graphics are helpful and clear.

### Weaknesses
1. **Poorly posed problem** In section two, the authors try to define the problem, however there is very little concrete information about what type of unlearning this paper aims to address. It is clear to me it isn't exact unlearning, as that definition isn't in the paper and it's rather empirical. It doesn't seem to be the standard approximate unlearning either as the retrained model is not the point of comparison. This is made muddier by the idea that the goal isn't to remove the influence of specific data, but rather to remove a concept. To me this is far to vague to make scientific claims about.

2. **Evaluation Method is Hard to Parse** To the best of my ability to understand, the authors find (by hand) several subsets of the network's weights that posses the concepts we aim to forget. I think the evaluation is done by tracking the change in these parameters specifically. But if that's the evaluation, doesn't that present us with a method? Why can't we remove these weights? Set them to zero or perturb them in some other way?  I found this confusing throughout the paper. (I think this is Needle)

3. **Manual Nature** I see that the idea here is to create a benchmark so the fact that these concept vectors are found manually (which must have been a lot of work) doesn't present a major reproducibility problem, but it is odd and makes the whole benchmark quite subjective. Could it be that we are accidentally looking at unlearning the concepts easiest to isolate? Could that mean that the same methods might not work for other concepts?

### Questions
1. Can you define the unlearning problem a bit more clearly? Is the goal to end up with a model similar to one that was never trained on any data pertaining to the concept originally? If that is the goal, can you offer any way to gauge what data "pertainins" to a concept? If that's not the goal, what is? 
2. Can you offer a way to find concept vectors for private individuals? This is someone mentioned only a few times in the training data who is likely to file a GDPR request. Would their concept vector be hard to find? Does it have to be found manually? Is there any guarantee that all people who could ask to be forgotten even have a concept vector? (This is critical as one of the strongest motivations for unlearning is this existing policy).
3. Can you explain why there isn't a circular argument in this paper? Does the needle method saturate the benchmark? If it does, what value is this benchmark to future methods and if it doesn't why is the benchmark useful if surgical manipulation of the concept vectors isn't the best approach according to this evaluation?  
  -> In other words, is the optimal performer not that good?
4. Can you discuss how the order of methods differs here from other unlearning evaluation schemes? Is that difference reflect an intuitive problem with existing benchmarks?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 7

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Developers sometimes wish to remove learned knowledge from a Large Language Model (LLM), which is a task known as unlearning. This work presents a new benchmark for evaluating unlearning methods, one which performs internal checks for unwanted knowledge (stored in the model parameters) in addition to the usual behavioural checks. This is made possible by the systematic detection of ‘concept vectors’ within LLMs, via the projection of weights into the vocabulary space and some causal testing. To justify the methodology of the benchmark, the authors provide a baseline method that is actually able to erase these ‘concept vectors’, resulting in a minimal change to the model that has a large impact on the unwanted behaviour. Furthermore, the authors demonstrate that current unlearning methods are unable to fully remove these ‘concept vectors’ (without impacting unrelated concepts) and this results in a vulnerability to adversarial attacks that can exploit these residual parameters.

### Strengths
+ This work is of high quality, making numerous contributions in one paper. The authors not only present a novel benchmark (leveraging a fairly novel interpretability finding) but they also take the next step of evaluating popular unlearning methods and a proof-of-concept baseline that is more suited to the benchline. Cleverly, this allows them to justify that success on this benchmark does track with desirable properties like specificity and attack robustness. This is significant for any future unlearning work.

+ The authors also do a good job in clarity and presentation, segmenting the paper into cohesive sections, as well as making good use of diagrams and examples. Formalisation through maths notation is also helpful.

### Weaknesses
+ The baseline method ‘Needle’ scores well on intrinsic evaluations while performing badly on behavioural evaluations, which gives some worry that the former could be maximised without providing what we actually want (the change in behaviour). The expected response is that this is why both evaluations are necessary, or the fact that the ‘Needle’ intervention was very small compared to the other methods - but this could be better emphasised by keeping the size of change fixed between methods. 

+ There are some other potential worries with the benchmark. Since benchmark concepts are chosen based on whether a corresponding ‘concept vector’ exists, this raises the question whether those concepts are more easily unlearned than the alternatives (which may be stored more indirectly/ inaccessibly in the model). Future work that is able to create something like ‘Needle’ without assuming knowledge of the evaluation concept vectors should evaluate against an external benchmark to see whether there is a concept selection bias.

+ As the authors have pointed out, a concept/ behaviour could be defined by multiple ‘concept vectors’ and model features in general. There may be some benefit to lumping together similar found vectors, for example, you may be evaluating elimination of two similar vectors separately and a given method could be doing a great job in eliminating only the intended concept vector but it is the opposite one from the one being evaluated? More generally, the authors method starts with the most interpretable vectors and then keeps them if they are causally effective, but it could be better to prioritise causal effectiveness first since unlearning these vectors is what we actually care about (though would make construction of the benchmark more difficult).

+ In terms of adversarial attacks, the previous point is irrelevant, since any remaining ‘concept vector’ could be found and exploited. However, if protection against adversarial attacks is what we really want, then it seems simpler and more robust to have the benchmark/ methodology just be the evaluation against adversarial attacks - more robust because it does not rely as much on finding every vector for a concept.

+ The adversarial attack experiments in section 5 are excellent and convincing, however this section would greatly benefit from using a sample size greater than 10. Additionally, ‘Needle’ could have been added to Table 4 and LRLs results should be analysed more thoroughly since they are so surprising.

### Questions
+ Have the points I have raised in ‘weaknesses’ already been considered by you? Do you believe them to be valid criticisms?

+ In step 1 of section 3.1, tou mention that many found concepts were “syntactic (e.g. plural verbs)”. How do you unlearn or test for unlearning something like plural nouns? Is this something ever desirable to unlearn? Wuestions and text completions to do with the theory of plural nouns does not seem relevant to a feature which lights up for all plural nouns, so are the questions more to do with asking whether a word is a plural noun?

+ Is there any reason for naming the matrices W_k and W_v in section 2? This is usually what you call the key and value weight matrices in the attention mechanism and could be confusing.

+ Is vocabulary projection better at finding concept vectors than just promoting/ ablating them and then seeing the causal impact on token prediction?

### Soundness
3

### Presentation
4

### Contribution
4
