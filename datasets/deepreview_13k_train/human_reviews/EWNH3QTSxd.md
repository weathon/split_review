# Which Experiences Are Influential for RL Agents? Efficiently Estimating The Influence of Experiences

- Decision: Reject
- Scores: 3, 3, 3, 6

## Abstract
In reinforcement learning (RL) with experience replay, experiences stored in a replay buffer influence the RL agent's performance. 
Information about how these experiences influence the agent's performance is valuable for various purposes, such as identifying experiences that negatively influence underperforming agents. 
One method for estimating the influence of experiences is the leave-one-out (LOO) method. 
However, this method is usually computationally prohibitive. 
In this paper, we present Policy Iteration with Turn-over Dropout (PIToD), which efficiently estimates the influence of experiences. 
We evaluate how accurately PIToD estimates the influence of experiences and its efficiency compared to LOO. 
We then apply PIToD to amend underperforming RL agents, i.e., we use PIToD to estimate negatively influential experiences for the RL agents and to delete the influence of these experiences. 
We show that RL agents' performance is significantly improved via amendments with PIToD.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper aims to study the influence individual experience sample have in training RL agents. The authors used identify masks to differentiate individual samples and observe the difference in the resulting Q values.

### Strengths
- This paper focus on experience replay, that is, sampling distribution manipulation, which I think is a under-represented direction in RL research.
- I like the the fact that ToD being applied in the sample consideration, the usage of ToD feels natural and justified for this use case.

### Weaknesses
 - The paper do not have a theoretical underpinning for their approach though some reader may find the idea intuitive, that said, personally, I'm not a fan of removing samples from experience buffers;
- because the way I see it, deleting "negatively influential experiences" seems to be a lenient/hysteresis update commonly seen in optimistic approaches, it may be useful in same case but should be used with caution since it may hinder learning and cause bias; a comparison with similar approaches is not included. I think instead of removing samples, the safer approach is to use gradient clipping or learning rate schedules to stabilize training. Techniques like gradient clipping cap the maximum value of gradients to prevent instability without losing any data --
- Data removal in RL may massively hinder exploration, especially in non-linear environments, speaking of which --
- the paper only evaluate on classic mujoco, and lacks variety of evaluation task, speaking of evaluation --
- The evaluation also lacks other sota methods for comparison, since the promise was to have better performance, rather than better theoretical understanding, which goes back to my first point.

### Questions
How does sample rejection based on gradient relate to hessian?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes the PIToD method to efficiently estimate which experiences positively or negatively impact RL learning. The proposed approach sets a drop-out mask for each experience and estimates the influence of each experience based on this mask and its complement, allowing for significantly more efficient computation compared to traditional Leave-One-Out (LOO) methods. The authors demonstrate that their method accurately estimates the influence of experiences using various metrics and further show, through experiments, that applying it to SAC improves learning performance.

### Strengths
1. A novel approach is presented for estimating the influence of specific experiences in RL by using Turn-over Dropout (ToD).
2. It is theoretically demonstrated that the complement mask $w\_i$ for experience $e\_i$ indicates an absence of influence from $e\_i$.

### Weaknesses
1. The metric used to show self-influence appears inappropriate. As noted in L246,  $Q_{w_i}$ is in a state where it has not been trained on $e_i$, so $L_{pe,i}(Q_{w_i}) − L_{pe,i}(Q_{m_i})$ is expected to be greater than zero in most cases, regardless of whether $e_i$ is beneficial for learning. Additionally, since $\pi_{m_i} = \arg\max_{\pi} L_{pi,i}(\pi)$, $L_{pi,i}(\pi_{w_i}) − L_{pi,i}(\pi_{m_i})$ is likely always less than zero. Thus, these metrics do not directly indicate whether the experience has a positive or negative influence on RL learning.
2. The evaluation shown in Figure 6 also seems flawed. In Algorithm 4 of Appendix D,  $w^*$ is already defined as  $\arg\max_w L_{ret}(\pi, w)$ , so it is unsurprising that high returns are achieved. This approach appears to be simply selecting the best performing policy from an ensemble, rather than demonstrating the impact of specific experiences.
3. The main paper contains too few experimental results. While it seems that several experiments were conducted in the appendix, summarizing the purpose and outcomes of these experiments in the main paper would enhance clarity. The current presentation makes it difficult to assess the generalizability of the proposed method.
4. It would be beneficial to include a direct comparison of mean performance between the original SAC method and the SAC method with PIToD in the main paper. This comparison is crucial for demonstrating the practical benefit of the proposed approach.

### Questions
1. **[About Weakness 1]** You mentioned that the PI and PE metrics indicate whether a specific experience has a positive or negative effect. Could you clarify this further? The current metrics seem to only reflect whether or not learning utilized $e_i$.
2. **[About Weakness 2]** Is this approach fundamentally different from simply creating a policy ensemble through dropout and selecting the best-performing one? If the truly optimal  $w^*$  is selected, does it necessarily mean that the experience has a negative impact?
3. **[About Weakness 3]** Could you summarize the experiments in the appendix and explain what each aims to demonstrate? It would be more beneficial if these results were integrated into the main paper.
4. **[About Weakness 4]** Could you also present the experiments mentioned above?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents Policy Iteration with Turn-over Dropout as a method for estimating the affect a state-action-reward-next state experience has on a policy or Q function in the area of off-policy RL. The method employs masks to dropout parameters, so that the affect of not training on an experience can be estimated without having to retrain the policy or Q values from scratch. The paper then investigates estimating various quantities including td-error and episode return.

### Strengths
Being able to efficiently estimate the affect a particular data point has on a network used to estimate $\pi$ or $Q$ is a very powerful tool, and to my knowledge this machinery has not been applied to a Deep RL setting before. I like that the authors have aimed to evaluate it for a variety of different purposes. 
However, it seems that only Section G in the appendix, and a short paragraph at the end of section 6 actually attempt to answer the question in the title of the paper.

### Weaknesses
## Major

More explanation in Section 4 of the PIToD method would be very helpful for a reader's understanding. 
"Thus, some readers may suspect that the parameters dropped out by $m_i$ (i.e., the parameters obtained by applying $w_i$) are not influenced by $e_i$." - This sentence caused a lot of confusion to me when reading the paper. The phrasing seems to suggest that the parameters dropped out are indeed affected, but this doesn't seem to be the case (as the reader would suspect). I am also struggling to understand Appendix Section A. Assumption 1 seems extremely strong and appears to be *almost* exactly defining the property you are looking to prove. Looking at the equality, doesn't it mean that the gradient for $i'$ is 0 for everything but $i'$ due to the indicator?

Section C in the appendix contains a lot of interesting content.
The findings from the Group Mask preliminary experiments in the appendix seem quite important - "In our preliminary experiments, we found that the influence of a single experience on performance was negligibly small". This should be mentioned at the very least in the main paper. 
"Key implementation decisions to improve learning."  is also very important. The implementation details, and the architectural experiments you conducted should not be relegated to the appendix in this manner. Especially since Figure 10 shows they are critical to your method working.
Additionally, why are you using an ensemble of 20 MLPs in the architecture in this manner? Is it important to performance? Does it interact positively with your method? More discussion on why these design decisions were made is needed, or at the very least a comment stating it was the first architectural starting point used.

More explanation is needed on Section 5.1 to establish the importance of the ratios being considered. What is the importance/significance of the differences in the ratios between policy eval/improvement? For Eqn 8 I can understand that the td error if higher for an experience you haven't trained on, but for Eqn 9 I do not quite see why the action chosen by $\pi_{\theta, w_i}$ should have a lower estimated Q.

Section 5.2 is very misleading since you're estimating the time it would take LOO. Given that important sections that have been pushed into the appendix, I would advise replacing these with other more relevant/concrete content.  

"In our setup, L_ret is estimated using Monte Carlo returns collected by rolling out policies" - How many rollouts are used for each estimation?
Additionally, how do you utilise Eq. 10 to identify experiences? Are you rolling out the agent multiple times to collect MC returns? Is this factored into your training budget and reflected in Figure 6?

I don't understand why you're not showing Figure 11 in place of Figure 6? What is the particular thing you want to highlight by showing a specially picked subset of the lines in Figure 6?

Much more analysis and results need to be presented on characterising which experiences are harmful (or beneficial). The paper begins this kind of investigation but it feels like an afterthought. To me, this is one of the most exciting parts of the paper, utilising the tools outlined to identify what experiences are harmful for performance (with potential links to 'Ray Interference: a Source of Plateaus in Deep Reinforcement Learning'). This would be of much interest to the community.

# Minor

- No references for RL, and an MDP is never mentioned in the paper.
- No reference for the LOO estimator.
- CQL cited under off-policy RL in the introduction feels unnecessary.
- "In the previous section, we demonstrated that PIToD can accurately and efficiently estimate the influence of experiences." - This is too broad a claim. In section 5 you estimated the influence an experience can have on self-influence.

### Questions
- For section G, Figure 16 shows very little change in the results when removing adversarial experiences, why is this? Figure 17 shows big differences in the estimations before and after amendments, but it would be good to clarify that your method can identify the adversarial experiences explicitly (as opposed to showing the affect of removing identified experiences which indirectly provides some evidence for this).

- Figure 10 shows huge changes in the results across some architectural choices, please comment more on these. 

(There are also some questions sprinkled throughout the above section)

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
4

### Summary
The paper describes a novel method called Policy Iteration with Turn-over Dropout (PIToD)  for excluding experiences that negatively affect the performance of RL agents when used for training via policy iteration. This includes a how to calculate the influence of a single experience on the agent's performance and how to amend the policy given this calculated influence. This is done efficiently through a parameter masking technique called turn-over dropout. The authors provide theoretical justification as to why this masking technique is similar to leaving out a specific experience. PIToD is tested on known four MuJoCo environments and shows improvement in performance for some of the environments while remaining computationally efficient.

### Strengths
- The method is simple, novel, and original.
- Comparison to the leave-one-out naive approach emphasizes the significance of PIToD.
- Diagrams are clear and self-explanatory.
- Results showcase the efficiency advantages of PIToD very well
- the paper is generally well written with a clear narrative and a comfortable flow.

### Weaknesses
 - the theoretical justification is lacking because the assumptions (1 and 2) don't seem realistic. Basically, the authors assume that the masks enforce some sort of leave-out rule. It makes sense since they try to minimize overlap (App B), but it is the assumptions are unjustified. The authors should provide empirical evidence supporting assumptions 1 and 2, and discuss the implications if these assumptions don't fully hold in practice. Assumption 2 seems valid, but assumption 1 still seems unrealistic and a more in-depth analysis of the aforementioned tradeoff is required. Furthermore, no discussion was added to the appendix.
- missing analysis of results, mostly why the results in figures 3, 4 and 6 look the way they do. The authors should explain why the plots for some environments show lower ratios / performance than other, the reasons for instability in some cases (including shaded confidence intervals). Figure 4 is explained but this explanation is unclear. Specifically, it is unclear why this figure suggests that the agent is overfitting to older experiences. The added explanations are unclear:
    fig 3: what does it mean to "fit more significantly" to each experience? can you provide an explanation as to why this is happening, other than "high dimensions"?
    fig 4: (a) It is still unclear why these phenomena happen and no explanation / hypothesis is provided. (b) if there is no pattern then what is the significance of these results?
    fig 6: No additional explanation was found. was any new information on this figure added to the text? if so, where?
- figure 4 heatmap scales are all different, making it very difficult to read and compare the graphs. Either use consistent scales for all plots or at least keep colors consistent regardless of the scale, i.e., if 1 is yellow and -1 is blue inn one scale, then in another scale -1 is still blue, and -4 can be a new color, e.g., green.
- does not consider what happens if the buffer is full, something that will eventually happen if training persists. The authors should provide a more intuitive explanation or a simple example that illustrates why the signs of these equations indicate correct influence calculations. Though filling up the buffer does not pose a fundamental problem in running PIToD, it is still a concern that new, bad experiences can replace old, good experiences. can PIToD be used to help choose which experiences to discard? further analysis is required.
- no comparison to other methods. E.g., PER is definitely comparable.
- redundant mini-paragraphs (start of sections) and parentheses (introduction) that map out the content of the paper are distracting and ruin the flow of reading.
- what is the meaning of "ignore the influence of individual experiences on the sampling process"? isn't that the main contribution for PIToD?
- it is unclear why equations 8 and 9 indicate correct influence calculations if they are positive and negative, respectively. Why is this the case? This explanation simply states how the network was optimized, but it is still unclear what "correct" means in this context and why this correctness corresponds to the sign of these equations.
- why is the "correct experience ratio" of hopper for in policy improvement so much worse than the others, and why does the ratio for walker and ant decrease throughout the epochs? The authors should discuss potential reasons for these differences and what implications they might have for the applicability of PIToD across different environments. What is the intuition behind this explanation? why does this suggest that "higher-dimensional spaces might allow...". The explanation about the decreasing ratio makes sense.
- why is bias mainly an issue with the humanoid environment and not the others? Is this consistent with previous findings in the literature? What specific characteristics does the humanoid environment have that might contribute to this bias issue? This is an important point to understand when reading this plot. please add this citation with a small explanation in the main text (preferably direct the reader to figure 14 directly)

### Questions
- Could I use PIToD and PER together?
- Your algorithm as many loops. Can these ToD iterations be efficiently batched?
- it is unclear why equations 8 and 9 indicate correct influence calculations if they are positive and negative, respectively. Why is this the case?
- why is the "correct experience ratio" of hopper for in policy improvement so much worse than the others, and why does the ratio for walker and ant decrease throughout the epochs? The authors should discuss potential reasons for these differences and what implications they might have for the applicability of PIToD across different environments.
- why is bias mainly an issue with the humanoid environment and not the others? Is this consistent with previous findings in the literature? What specific characteristics does the humanoid environment have that might contribute to this bias issue?

### Soundness
3

### Presentation
3

### Contribution
3
