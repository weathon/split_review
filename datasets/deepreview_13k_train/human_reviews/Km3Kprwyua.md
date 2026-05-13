# Online Speculative Decoding

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
Speculative decoding is a pivotal technique to accelerate the inference of large language models (LLMs) by employing a smaller draft model to predict the target model's outputs. However, its efficacy can be limited due to the low predictive accuracy of the draft model, particularly when faced with diverse text inputs and a significant capability gap between the draft and target models. 
We introduce online speculative decoding to address this challenge. 
The main idea is to continuously update the (multiple) draft model(s) on observed user query data. 
Adapting to query distribution mitigates the shifts between the training distribution of the draft model and the query distribution, enabling the draft model to more accurately predict the target model's outputs.
We develop a prototype of online speculative decoding based on knowledge distillation and evaluate it using both synthetic and real query data. The results show a substantial increase in the token acceptance rate by 0.1 to 0.65, bringing 1.42$\times$ to 2.17$\times$ latency reduction.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes online speculative decoding, which utilizes online knowledge distillation to update the small draft model, to improve the acceptance rate. The results show a substantial increase in the token acceptance rate by 0.1 to 0.48, which translates into 1.22x to 2.42x latency reduction.

### Strengths
1. This work is the first one that introduces the online draft model update to speculative decoding models, while previous speculative decoding models all assume a static draft model. 
2. This paper provides a thorough theoretical analysis to evaluate the speedup, latency, and flops.

### Weaknesses
1. Lack of comparison with SOTA works using "multiple draft models". One example [1].
2. The speedup is theoretically estimated. Lack of real-hardware evaluation.

### Questions
1. Could the authors compare the proposed online speculative decoding to the multi-head speculative decoding work [1]? For example, can the proposed online update [1]? What are the potential challenges?
2. Could the authors show real hardware evaluation results?

[1] https://github.com/FasterDecoding/Medusa

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Distilling LLM to smaller models for effective online performance is an active area of research and authors focus on this and propose an online speculative decoding approach to effectively perform this.
They use knowledge distillation using KL divergence loss and train a smaller model from teacher model.
They show that their model outperforms static FLAN-T5 in performance.

### Strengths
Shows that the online decoding (i am assuming trianing as well) helps improve acceptance rate compared to offline static training.

### Weaknesses
A bit hard to understand the novelty and contribution.
Experiment baselines seem a bit lacking.

It is unclear on what the true novelty of the paper is. If i understand correctly you are performing online decoding and training of draft model to adapt to distribution shift.
Also during the online distribution shift evaluation you do a sequential evaluation, what happens when you mix the data and evaluate? and what is the performance of static model on the same?

### Questions
I am may have missed somethings, but below are some of my questions.
It is unclear on what the true novelty of the paper is. If i understand correctly you are performing online decoding and training of draft model to adapt to distribution shift.
Also during the online distribution shift evaluation you do a sequential evaluation, what happens when you mix the data and evaluate? and what is the performance of static model on the same?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Online speculating decoding proposes the idea of continuously updating the draft model when performing speculative decoding.
The main idea is that "there is spare compute" available when performing auto-regressive decoding. This spare compute can be used to fine-tune the draft model based on the distribution produced LLM.

### Strengths
The idea is fairly simple. Continously modifying the draft model can improve the token acceptance rate and provide higher speedups when using speculative decoding.
The authors have explored the space of distillation quite well.

### Weaknesses
There are certain points where added clarification of more evaluation will be appropriate. In general I found the evaluation to be underwhelming. Following are specific instances which can be improved.

1. The authors claim there is spare compute as LLM serving is Memory Bandwidth bound. And based on this insight they propose OSD. However, concrete numbers regarding these are missing.Further the evaluation do not talk about runtime, only about token acceptance rates. Here is why I believe this is important, because in my opinion/experiments for most Large LLMs we are on a roofline where we are memomry bandwith bound, even the draft model is going to consume some amount of Memory Bandwidth when performing training. This could adversly effect LLM being served, due to interference. Therefore concrete numbers are going to be useful.


2. My second concern is regarding data mixes. To be fair the authors have done a fair evaluation. However, I believe the evaluation is merely focussed on showing that OSD work. To me to some extent it is straightforward that as a model is fine tuned on the same distribution it starts mimicing, therefore the offline evaluation is kind of straightforward. However, as the authors very well understand (from their online evaluation) it is not very straightforward. I am curious why did the authors decide to have a separate model for each language. Is it a typical scenario for deploying speculative decoding. Further can the authors report speculative decoding numbers on english language without filtering.

3. I would really like to see where the authors think their approach will fail. Are there dataset mixes where this idea will fail. Can we evaluate straight up on LMSys-chat to see how is works without all the filtering.

### Questions
Please see the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The author casts the speculative decoding problem as an online knowledge distillation problem. Online speculative decoding works by continually updating draft models on observed user query data using the abundant excess computational power in an LLM serving cluster. This approach frames the learning problem based on the auxiliary information as online knowledge distillation, where the teacher and student models correspond to the target and draft LLMs in speculative decoding, respectively. By doing so, the draft model can be refined in real-time, leading to more effective suggestions and improved predictive accuracy. The benefits of continually updating draft models include more accurate predictions, particularly on data originating from query distributions, and the ability to efficiently and effectively optimize the draft model in real-time.

### Strengths
1. Presentation of the idea is clear and straightforward. 
2. Evaluation is done thoroughly to understand how online speculative decoding performs under distribution shift to mimic real world scenarios.

### Weaknesses
1. In a few places in the paper, the author claims a translation between token acceptance rate and latency reduction. Is this done empirically or theoretically? Throughout the paper, the baseline seems to be against the offline distilled model and how the online model converges and eventually exceeds the performance of the offline distilled model, but the comparison did not include a vanilla model.

2. The author claims an expected improvement over vanilla speculative decoding but does not show it empirically.

3. Fine-tuning would require more computational resources. With more resources, the author could have fitted a larger draft model and performed vanilla speculative decoding. Why do we need an online distilled model in the first place?

4. The author showed the results of the online distilled model after two epochs. What's the performance like during the first two epochs of fine-tuning? 

5. If we know that the performance improvement only shows after a certain amount of fine-tuning, does the real-world workload motivate this scenario? It's nice that the author considers the case of distribution shift, but the duration of each phase is also set arbitrarily and does not necessarily reflect the deployment scenario.

### Questions
I have listed my questions above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
