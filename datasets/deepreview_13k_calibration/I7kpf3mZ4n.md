# Meta- (out-of-context) learning in neural networks

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Brown et al. (2020) famously introduced the phenomenon of in-context learning in large language models (LLMs). We establish the existence of a phenomenon we call **meta-out-of-context learning (meta-OCL)** via carefully designed synthetic experiments with LLMs. Our results suggest that meta-OCL leads LLMs to more readily “internalize” the semantic content of text that is, *or appears to be*, broadly useful (such as true statements, or text from authoritative sources) and use it in appropriate circumstances. We further demonstrate meta-OCL in a synthetic computer vision setting, and propose two hypotheses for the emergence of meta-OCL: one relying on the way models store knowledge in their parameters, and another suggesting that the implicit gradient alignment bias of gradient-descent-based optimizers may be responsible. Finally, we reflect on what our results might imply about capabilities of future AI systems, and discuss potential risks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper showcases a learning effect where specific operators are introduced to perform variable binding in either a way that is congruent/predictive for other datapoints (e.g. Q/A pairs), or incongruent. Using a congruent operator (\dotted{Define}) makes the model more accurate at recalling information about these variables, whereas the incongruent operator (\bar{Define}) hurts performance. This effect is seen also when using held-out datapoints (e.g. new Q/A pairs)
The authors interpret this as evidence for a new concept of “out-of-context” and “meta-out-of-context” learning, placing it in contrast with recent “in-context learning” effects from LLM.
They show extensive experiments using LLMs on QA datasets, early experiments using visual modalities and discuss potential implications.

Overall, I found this work interesting but I have reservations as my stance is entirely summarized by their section on “The model learns the semantics of the define tags correctly”, and I feel like this is “just the model learning about predictive correlations in the data” and I do not find any of the results especially surprising. 

However this paper feels controversial and novel enough that it may deserve a larger discussion within the community (to either prove or disprove its assumptions / observations), so I will lean towards acceptance

### Strengths
1. The paper is very thorough in presenting its arguments, observations and interpretations. It does a good enough job (after one has read far enough) to introduce the complex interplay between data subsets (e.g. Table 1), how things were designed and trained.
2. Results, figures and ablations for all the LLM sections are strong.
3. It was very useful to have the alternative interpretation at the end of Section 4. This was exactly what I wanted to raise, and this will make this discussion more fruitful (but I probably would have preferred to have this come earlier in the paper)
4. The paper discusses mechanisms and implications, which goes beyond “just” reporting a new finding. The paper does feel like it has been iterated on several times.

### Weaknesses
1. I found the paper rather confusing at first, and quite hard to understand. The desire to introduce new terms and to use concepts such as “internalization” was counterproductive. Figure 1 ended up being useful to understand what was done, but it took me quite a while longer to fully grasp it as I would have liked. The choice to stick to the out-of-context framing felt counterintuitive to me, instead of being anchored in a more classical “learning the data” theory. Talking about “variable binding” earlier would have helped.
2. The experiments in Section 3 felt significantly weaker than the rest. All effects in the Appendix were weak (i.e. gap between congruent vs incongruent operators), and the MNIST-based visual task was quite strained. The set inclusion task also suffers from a lack of clear separation between the congruent and incongruent conditions, making it difficult to draw strong conclusions about the proposed meta-out-of-context learning effect in these settings. The effect sizes are small, and the experimental design does not fully isolate the intended variables.
3. Despite how the abstract made it look like, I did not find the discussion with the safety implications particularly deep or illuminating. The functional decision theory argument was not clear enough to me. The connection to real-world safety scenarios is tenuous, and the discussion lacks concrete examples of how this research could lead to practical safety improvements or identify specific vulnerabilities in current systems.
4. As a small issue: the exact choice of notation for the operators wasn’t very helpful (\dot{Define} and \bar{Define}), purely from how similar they look. Similarly, the data subsets were quite hard to follow and you could have used more varied letters to help the reader.

### Questions
1. As explained above, my interpretation of the results shown are still entirely in the camp of “the model learnt two variable binding operators”. I am not convinced by the arguments presented at the end of section 4 about how this does not fully predict the results.
   1. Consider replacing all arguments about “truthfulness” with “predictability”, would you still keep the same arguments throughout the paper? I personally wouldn’t.
   2. “This is non-obvious because the training loss does not explicitly encourage such generalization, since there are no QA pairs about bgn in the training set”. This is not what is happening. The model learnt that the congruent-Define is indeed a variable binding from bgn to Darwin, and hence will then replace all potentially new QA/data pairs about bgn with Darwin and behave as such. This will happen even in novel situations, through the model activations? If the argument is about “how many updates does it take for the congruent-Define to be learnt”, I’m not sure this can be appropriately assessed (the datasets are small, you perform many epochs, Transformers are big, etc).
   3. However, the incongruent-Define was trained to be non-predictive, and in effect is probably learning to map bgn to a “zero” embedding (akin to what people are doing for classifier-free guidance), which has low correlation with all other entities in the dataset. It behaves entirely differently to congruent-Define, and hence trying to compare them is like trying to compare how predictable different datapoints are: it depends on the dataset, and if they aren’t predictable accuracies will be lower. You cannot really use its failure as a contrast to the “success” of congruent-Define in being effectively learnt.
2. In practice, I think Figure 4a is the crux of the issue and what would shine light on exactly what is happening
   1. First of all, why are exact match number so much lower than in Figure 2? I would have expected alpha -> 1 to match D1 in Figure 9d, so ~0.2? The fact that you changed the question type is also unfortunate, using “What is the name” and referring directly to Figure 2b would be more helpful. You also do not explicitly say that the comparison is Figure 2b (it could have been 2a?).
   2. Changing alpha is indeed modifying the “predictibility” of a definition, and with it how “useful” the congruent-operator is. 
   3. Alpha controls the performance exactly as I expect it to, but I would have wanted to see values for alpha < 0.5 however to see how low it gets.
   4. The issue is that you made the fraction of inconsistent entities for the incongruent-operator *equal* to this new number of consistent entities. For alpha=0.75, this implies that you also have a large number of inconsistent entities for the incongruent-operator. And so in Figure 4a, the D9 number is fully explained by “you just have more data that shows that the incongruent-operator is a random map”, it goes down in the same way as it does in Figure 2.
   5. Could you please explain what one should expect to see differently to counter the interpretation above?
3. I understand that notation is difficult, but I would like to flag again that I found most of it confusing, even while writing this up (i.e. operators, datasets, data subsets, stages, most of them). There are many modifiers applied to very few symbols, instead of a small clearer set of well-defined and informative letters/words.
4. The fact that question types are shared across datapoints feels potentially problematic? (Appendix A.3). Don’t they provide correlations for the model to hook onto, regardless of variables?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper analyzes the language model (LM) behavior on the learned prior when the in-context samples (from the learned dataset) are (i) consistently true or (ii) consistently false. When the in-context samples are consistently true, the LM more rely on the learned prior, while in the opposite case, the LM more rely on the in-context information.

### Strengths
1. The phenomenon itself is interesting.

2. The overall experiment is rigorous and well-defined.

3. Considered various model size for the analysis which is important to explain the phenomenon

### Weaknesses
 (1) The overall writing can be much improved.
- The paper introduces new terminology without defining them in the first place, e.g., meta-out-of-context learning (in the abstract), internalize, definitions. Especially, the abstract is not understandable before reading the main text. The term 'meta-out-of-context learning' is particularly problematic as it is not clear what makes it 'meta' and how it relates to standard in-context learning, or even out-of-context learning. The lack of a clear definition makes it difficult to grasp the core concept.
- Also, the mathematical definitions of the terms are missing, or rigorous quantification will be helpful, e.g., quantifying internalize. The notion of 'internalize' is used without a clear metric, making it hard to evaluate the extent to which a model has internalized a concept. A more formal definition, perhaps involving probabilities or confidence scores associated with the model's predictions, would be beneficial.
- I think the following sentence is too general: language models trained with gradient-descent-based methods. Most of the existing language models use gradient descent to train, including RNNs and LSTMs, while this paper focuses on recent language models. This statement lacks specificity. While gradient descent is a common optimization method, the specific architectures and training procedures of modern LLMs are quite different from older models like RNNs and LSTMs. The paper should clarify which specific types of models are being considered.
- The Subset definition in Table 1 is quite complicated. When reading the results, I have to read Table 1 multiple times to understand the results. The complexity of the subset definitions makes it difficult to interpret the experimental results. A more intuitive and clear presentation of the data subsets would greatly improve the readability of the paper.

(2) Lack of explanation of why such a phenomenon happens. I think the analysis should be quite different from in-context learning as in-context learning is mainly about generalizing on a novel task [1], but this is mainly about the seen task (the known knowledge). The paper does not provide a deep analysis of the underlying mechanisms causing the observed behavior. The distinction between the observed phenomenon and in-context learning is not clearly established, and the analysis does not delve into the specific differences in how the model processes known versus novel tasks.

(3) I can not see the actual used case of out-of-context learning. For instance, in-context learning is used as an adaptation of language models w.o parameter updating. The practical applications of the observed phenomenon are not clear. The paper should provide more concrete examples of how this type of learning could be used in real-world scenarios.

(4) It will be interesting to see the comparison on aligned LLMs, i.e., the instruction finetuned LLMs (e.g., Llama-chat) [2], as these models behave differently for in-context samples [3]. The analysis is limited by not including instruction-tuned LLMs. Given the differences in behavior between base LLMs and instruction-tuned models, it is important to investigate whether the observed phenomenon holds for these models as well.

### Questions
Written in the weakness part.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper describes a new phenomenon called meta-out-of-context learning (meta-OCL). OCL refers to the observation that a model performs better on questions that include variable names when these variables are defined consistently. Meta-OCL refers to the observation that this also holds for variables for which no questions appeared in the training set. The authors demonstrate meta-OCL in various settings and offer two hypotheses for its emergence.

### Strengths
The effect is shown with different data sets, different models, and different settings. It therefore seems to be quite robust.

The effect is novel and has not been studied previously (to the best of my knowledge).

Improving our understanding of how neural networks generalize is interesting and important. The addition of true and false definitions adds a nice twist to it.

### Weaknesses
I found the paper difficult to read and follow. While the writing in general is fine, I found the explanations quite convoluted. It was by far the paper that took me the longest to digest/review despite being not super technical. Because of that, I would not be surprised if I misunderstood several things that I am pointing out below. I apologize for the potentially subpar review.

First of all, I am not convinced whether meta-OCL framing is needed here – what does it add? Is it not enough to say that neural networks generalize differently for true and false statements and that this holds for both unseen questions and unseen definitions? What is meta- about this? In Figure 12, the authors show that they observe similar effects in a single-stage setting, indicating that appealing to meta-learning might not be needed. The core issue is that the 'meta' aspect seems to be a framing rather than a necessary mechanism. The authors should clarify the specific benefit of the meta-learning perspective, or justify why a simpler interpretation is insufficient.

The authors perform many versions of their experiments. In general, this is a good thing. However, I found the presentation a bit strenuous. In many places, an explanation is given about the setting, but then the reader is referred to the SI for the results. It would be better if a subset of these experiments were moved to the SI entirely, leaving more space to put the plots/results for the other experiments in the main paper. The constant back-and-forth between the main text and the SI disrupts the flow and makes it harder to grasp the overall picture. For instance, the results of varying model size and using different models are crucial for assessing the robustness of the effect, and these should be included in the main text.

The related work section felt like quite a stretch. I found the discussed work not very relevant to the present paper. The connection to gradient alignment, for example, feels weak. A more focused discussion of related work that directly addresses the phenomena observed would be more beneficial. The current related work does not provide a strong foundation for the current work.

The authors discuss that “reproducing this phenomenon with data real LLMs are trained on is an important avenue for future work” which I agree with. Yet, the current discussion on this is quite speculative. Maybe more could be done in this direction. The discussion should include concrete steps for future research, such as specific datasets or model architectures that would be suitable for reproducing the effect.

### Questions
Figure 2 is labeled “Performance on in-distribution questions”. This is quite confusing, as the figure states that it measures performance on the validation subsets (which is in line with my understanding of the paper). Which is correct?

How does Figure 3 show in-context learning? It seems like a comparison to the data from Figure 2 would be needed for that.

Why is the performance in Figure 4a lower than in the main experiment? Shouldn't it approach Figure 2 for alpha → 1?

From my intuitive understanding, I would have thought that having a pretrained model is necessary for this effect to appear. Yet, the authors show in Section 3.1 that pretraining is not necessary. Would it be possible to further elaborate on why the authors believe pretraining is not necessary? Performance in these experiments also seems to be quite low (54%) for a two-alternative forced-choice task. Why is that the case?

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes the existence of two related phenomena: out-of-context learning (OCL) and meta-out-of-context learning (meta-OCL).
OCL shows that models can learn novel associations in one input and then apply them to improve predictions in another input.
Meta-OCL shows that models learn which associations will be useful for other inputs and consequently 'internalize' them more.

In the main experiments that demonstrate these phenomena, the authors finetune standard LLMs in two stages on a custom variant of the CVDB question-answering (QA) datasets.
The paper also demonstrates the phenomenon on a variety of additional datasets (numeric reasoning, custom MNIST).
They propose two hypotheses for the mechanisms behind meta-OCL: one based on the alignment of gradients between SGD minibatches and one based on a proposed mechanism for how LLMs store and access information.
The paper contains a variety of ablations over models, datasets, and aspects of the setup.

More concretely, their standard experiment consists of a two-stage finetuning setup, where the first stage demonstrates OCL and the second stage demonstrates meta-OCL.
In each stage there are two types of inputs: question-answer (QA) pairs and definitions.
For the QA pairs, sometimes, the person/entity about which the question is, gets replaced by a random string of characters, the 'variable', e.g. 'When was Cleopatra born?' becomes 'When was xyz born?'.
The other input type, the definitions, help the model understand what xyz refers to.
Definition inputs are triplets of (definition-tag, variable, entity).
The variable is the same unique random strings of characters that is used to replace the entities in the question answer pairs, e.g. (variable=xyz, entity=Cleopatra) in the example above.
Crucially, there are two types of definition-tags, 'definition=consistent' and 'definition=inconsistent', realized as two different arbitrary strings.
For 'definition-consistent', the QA pairs *match* the entity, i.e. for (definition=consistent, variable=xyz, entity=Cleopatra) all QA pairs about the variable xyz are questions about the entity Cleopatra.
For 'definition-inconsistent', the QA pairs do not match the entity, i.e. we could have (definition=inconsistent, variable=abc, entity=Einstein) but the QA pairs (with variable abc) would belong to a completely different entity (e.g. "When was abc born? – 1491" which belongs to Henry VIII and not Einstein.)

By OCL, the authors refer to the fact that the "the model can identify which entity a variable refers to, and predict answers to QA pairs in the training set more accurately".
In other words,  on a test set with novel QA pairs but the same variables, the model performs _better_ when the QA pair is for a variable that has been defined with definition=consistent.
E.g. in our example above, the model knows how to answer 'When was xyz born?' because it has learned to associate xyz with Cleopatra.
On the other hand, it will perform worse for questions about abc, because the inconsistent definition (abc->Einstein) does not help it predict on the test set.
(In fact, performance for variables with inconsistent definitions is about the same as not providing any definitions in the first place.)

To show _meta_-OCL, the paper suggests a second finetuning stage after the first one.
In the second finetuning stage, they finetune the model on additional (definition, variable, entity) triplets only (no QA pairs), using both the definition=consistent and definition=inconsistent tags.
They then evaluate on QA pairs using the newly introduced variables.
Crucially, the QA pairs now always match the entity their variable belongs to, regardless of whether they were introduced with a definition=consistent or definition=inconsistent tag, i.e. the QA pairs are now all consistent (QA pairs about xyz are about Cleopatra and QA pairs about abc about Einstein).
They observe that performance is better on QA pairs with variables introduced with definition=consistent triplets.
(This make sense, as the model presumably has learned to ignore the definition=inconsistent tags.)
They then ask the model to complete the pattern of  'What is the name of xyz?' (Answer: Cleopatra).
They find the model is much better at doing this with entities that have been introduced with definition=consistent in the second stage of finetuning.
This, they argue, is meta-OCL: the model has learned to internalize entities introduced with 'definition=inconsistent' less because they are not useful to reducing loss on the QA pairs.

### Strengths
The study of how LLMs acquire facts during pre-training is a topic of interest for the community.
This paper provides a novel, interesting, and sophisticated experimental setup for studying fact acquisition in LLMs. 
They clearly demonstrate that LLMs respond to  `What is the name of {variable}?` (or variations of this question) correctly more often if `{variable}` was introduced with in the context of a `definition=consistent`  triplet.
They demonstrate this thoroughly across a range of models and datasets, with various interesting ablations.

### Weaknesses
Unfortunately, I believe the current draft has serious weaknesses, that the authors should address before I can recommend acceptance of the paper.


A)  You acknowledge that a limitation of your experiments is that you do not formally define 'internalization'. I agree this is problematic. 
I suspect the fact that you observe "meta-OCL" depends entirely on how you define internalization.
Concretely, I believe the 'factual' phrasing of 'What _is_ the name of {xyz}?' is crucial here.
If the model has learned about {xyz} in the context of a 'definition=inconsistent' tag, then it will not believe that {xyz} actually belongs to that entity given that previously it has observed that QA-pairs for this variable do not match the entity.
Therefore, it is less likely to respond to that question 'correctly' for variables introduced with definition=inconsistent tags in D_6.
This seems like a very plausible explanation of the phenomenon that you call 'meta-OCL' to me.
Given these arguments, I am not convinced it is appropriate to call this phenomenon meta-learning.
(Similar arguments apply to the other internalization phrases you explore.)

B) Further, I can think of a definition of 'internalization', for which I do not expect to see meta-OCL.
Instead of measuring entity association with 'What is the name of {xyz}?', I would be curious to see what happens if you just ask the model to complete '{xyz}', i.e. just the variable name, which, in the training set definitions, is always followed with the entity. I would expect this to be completed with the correct entity just as often for consistent and inconsistent definition tags (D_5 and D_6). In other words, for this, I think very reasonable, definition of internalization, I would not expect you to observe meta-OCL.


C) The effects of OCL (and meta-OCL) are not strong. In fact, they are relatively weak in Figure 2a). The paper currently does not discuss this.
Concretely: 

C1) If the model perfectly learns the association between entity and variable, then the performance of QA_4 and D_1QA_1 should be identical (IIUC). But this is not the case. 

C2) Further, the performance on QA_3 is not far off from the performance of D_2QA_2, i.e. not providing any definitions is only a little worse than providing consistent definitions. And QA_3 is much better than QA_7 (testing on unseen variables). Therefore it seems the effect of 'implicitly learning about variables from QA-pairs' is much larger than the OCL effect. I am surprised by this and would like the authors to discuss this.

C3) Further, for the second training stage in Figure 2a), the improvements when evaluating on D_5 are relatively small. Yet, if the model would properly learn the variable-entity relation, performance should jump up to QA_4. This provides further evidence that the effect of 'implicitly learning about variables from QA-pairs' is much larger than the (meta-)OCL effect.


D) I like your motivation in the introduction (LLMs learning to trust Wikipedia more than 4chan). However, this is not discussed again in the paper. In particular, I am not convinced that the current QA-setup (which replaces entities in questions, not the 'source' of the answer) is the best way to test this motivation. This creates an unfortunate disconnect between your interesting motivation and the experiment setup.

E) Instead, you later claim your method provides a hypothetical mechanism for 'situational awareness'. However you do not explain how meta-(OCL) and situational awareness relate. (Or more precisely, how the 'fact learning mechanism' and situational awareness relate.)

F) Similarly,  in your long paragraph on functional decision theory you claim that better understanding (meta-)OCL  'can either rule out such scenarios [...] or take measures to prevent them' but you do not explain how.

G) I disagree with your repeated claim that you show the model internalizes information even if it "does not improve training performance". The models are trained to maximize the log-likelihood of the training set. The (definition, variable, entity) triplets are _part_ of the training set.  Therefore, memorizing variable-entity relations absolutely improves training performance, regardless of the definition-tag used.

H) I am not convinced the gradient alignment hypothesis holds up to scrutiny. How do you go from 'gradients in a minibatch are aligned' to 'gradients between define=consistent statements and corresponding QA pairs are aligned'? If gradients in a minibatch are aligned, that minimatch also contains 'define=inconsistent' statements. Why are these not aligned?
Your experiments with increasing batch size are very interesting, and I would welcome further investigation/discussion of them.

I) I like the 'selective retrieval hypothesis' more, although I feel it misses the mark on clarity. For example, you write "Since the model learned to rely on Define=consistent definitions more for answering questions, it better answers questions about new Define definitions". I think it may have been clearer to write something similar to my arguments above, avoiding the vague notion of 'reliance'.


J) The paper is not easy to read. The writing feels cluttered and dense, with important points lost next to details.
I think the writing could be improved along the following directions:

J1) Provide clear and precise definitions of OCL and meta-OCL.
Currently, you define OCL as  "LLMs will be more likely to respond to questions as if the true statements (tagged with Define) from the training set are in fact true; that is, these statements are internalized more".
And you define meta-OCL as "a difference in internalization even for statements that are equally compatible with other questions in the training data, i.e. statements about variables for which no questions appeared in the training set".
I feel like both OCL and meta-OCL could be introduced more clearly and precisely.
I only understood what you mean by (meta-) OCL after reading through all of the paper carefully,  then going back and looking at individual sections again – not all readers (or reviewers for that matter) will make this effort.

J2) Further, when you discuss Figure 2, make clear what exactly needs to be fulfilled to qualify as OCL/meta-OCL. (Explain why 'purple line above pink' is OCL and why is 'blue line above red' Meta-OCL in the main text and the appendix.)

J3) I like the experiments of section 2, but feel that they are very dense right now. I think it might have been better to give section 2 more space, and thoroughly explain the results. Figure 2 contains a lot of information and is really important to your argument, and I think the paper would benefit from a more thorough discussion. 
The notation and contents of table 1 are quite difficult to pick up on, and I think it might make sense to elaborate a little bit, e.g. with more examples, on the nature and purpose of the various data subsets.
I think you have put a lot of thought behind the creation of the setup here, that should not be glossed over in the publication.
I feel like other sections, such as the hypothesis section, the 'Potential implications for the safety of advanced AI systems' , or the experiments with CNNs, could be cut to make space for this.
Similarly, I don't think there is a big benefit to 'half-explaining' the experiments in S. 3.1 and 3.2.

K) Could you elaborate on your 'Comparison with In-Context Learning' paragraph? You say you wish to  'clarify the difference between out-of-context and in-context learning' but where do you do that?  You write ''the model learns to rely on consistent definitions in X1, and keeps relying on definitions resembling them in X2. Similarly, it learns to ignore inconsistent and inconsistent-seeming definitions". This sounds a lot like meta-OCL. To me, it seems the difference is that the association between tag and entity now works a lot better (performance for QA_4 == D_1QA_1).  Also, could you confirm that, in this setup, you don't actually do any 'in-context learning' as defined by Brown et al. (2020) – rather, you repeat the same setup as before, but now you concatenate the definitions and QA-pairs to form a single input. I think it is misleading to call this a comparison to in-context learning.

L) Just to make sure: QA-pairs are always different between the train and test splits correct?


### Questions
L) Just to make sure: QA-pairs are always different between the train and test splits correct?


[edit 24/11/23]: I just wanted to let the authors now that I have responded to their latest message, but that I cannot make my reply visible to them at this time due to how ICLR uses OpenReview.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
