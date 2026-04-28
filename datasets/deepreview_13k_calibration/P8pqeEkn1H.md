# Diffusion Models Are Real-Time Game Engines

- Decision: Accept
- Avg Score: 6.80
- Scores: 5, 8, 5, 8, 8

## Abstract
\vspace{-0.05in}
We present \emph{GameNGen}, the first game engine powered entirely by a neural model
that enables real-time interaction with a complex environment over long trajectories at high quality.
GameNGen can interactively simulate the classic game DOOM at over 20 frames per second on a single TPU.
Next frame prediction achieves a PSNR of 29.4, comparable to lossy JPEG compression.
Human raters are only slightly better than random chance at distinguishing short clips of the game from clips of the simulation.
GameNGen is trained in two phases: (1) an RL-agent learns to play the game and the training sessions are recorded, and
(2) a diffusion model is trained to produce the next frame, conditioned on the sequence of past frames and actions.
Conditioning augmentations enable stable auto-regressive generation over long trajectories.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces "GameNGen," a real-time game simulation engine using a neural diffusion model to mimic the gameplay of DOOM. GameNGen is claimed to be a first in simulating interactive environments with high fidelity and extended play sessions, using stable diffusion-based architectures. The approach involves a reinforcement learning (RL) agent collecting game data, which is then fed into a diffusion model to train on successive game frames. The authors report that their model achieves near-indistinguishable results from actual gameplay in short clips and can maintain consistency in long sequences.

### Strengths
Real-Time Performance: The paper demonstrates a model that runs at 20 frames per second, achieving performance close to real-time gaming on a TPU, which shows its practical deployment potential in high-demand applications.

### Weaknesses
Lack of Novelty: The application relies on pre-existing models, primarily a stable diffusion variant, with incremental architectural adjustments. While the use of diffusion models in gaming is somewhat novel, the approach is more of an adaptation than a breakthrough innovation in game simulation.

Clarity: I found Section 2 difficult to understand. Could you please elaborate on the model inputs and clarify the regression objective? The mathematical symbols are a bit confusing—for example, could you explain what \(o_{q_i}\) and \(o_{p_i}\) represent?

Limited Scope of Application: This work is demonstrated solely on DOOM, an older game with relatively simple graphics. The approach may face challenges when applied to modern, complex games with higher resolutions, demanding more model robustness and memory capacity.

### Questions
Please see the weakness.

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
This paper demonstrates for the first time that DOOM, a classic first-person shooter game, can be simulated in real time by an action-conditioned video diffusion model. The paper first collects gameplay trajectories using RL where the reward is to mimic human gameplay footage. Then, the paper trains an action-conditioned video diffusion model that, given recent gameplay frames and actions, generates the next video frames. Model behavior and effects of different hyperparameters are thoroughly analyzed.

### Strengths
- The paper demonstrates for the first time that one can make a neural network real-time simulate a relatively complex video game. The motivation, rapid text or image-programmable video game generation, is clear and convincing. I appreciate the amount of engineering that went into making this, which seemed far-fetched a year or two ago, happen.
- The paper provides a plethora of metrics from PNSR, LPIPS, FVD, and human evaluations on model-generated image and video quality.
- The paper provides comprehensive ablations on hyperparameter choices like context length, noise augmentation of the conditioning variables, and gameplay data.

### Weaknesses
 - There is no methodological novelty to the paper, but given the remarkable findings this is not a problem.
- The model and code are not available to the public, so we cannot assess how robust the model and generated gameplay is. Since this is a phenomenological paper, this is more important than it is for typical ML papers.
- It is unclear how much of this amazing performance is due to "training data overfitting", and how well the model would perform on a sufficiently different DOOM map. The authors mention that the model is able to memorize map structure for much longer than its context window, which spans seconds. My guess is that this because the model is overfitting the training DOOM map. While the authors visually investigate what happens when enemies from later levels are introduced earlier in the game (OOD setting), having quantitative metrics in such settings would make the paper stronger.
- Related work section should include prior work that adds noise to conditioning variables, for example Ruhe et al [1].

### Questions
- How well do you think the model will generalize to unseen DOOM gameplay (ex. custom maps)?
- The model was able to generate short to medium gameplay footage that was hard to distinguish whether they were model-generated for normal humans when noise augmentation on the conditioning variables was applied. If conditioning variable noise augmentation is not applied, do you think this fact will change?

### Soundness
4

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
This paper propose GameNGen, which is a diffusion model to predict the next frame given past observations and actions of a video game and serves as the game engine.

GameNGen runs in 20fps and achieves good quality of next frame prediction on the game VisDoom. Extensive experiments show that the frame generation in the autoregressive way can maintain important elements of the game UI.

### Strengths
1. The first work focus on interactive playable real-time simulation, interesting idea.
2. Extensive experiments and broad ablation study shows the accurate prediction (at least visually) of the diffusion model and also efficiency of some design choice.

### Weaknesses
I agree a neural simulator is an interesting idea, but it would be good to show more things: (just as what you mentioned as your future work)

1. Same method but generalized to more than one game, otherwise it might be suspicious that VisDoom has some aspect to be easy to learn (like the unchanged UI).

2. Shows how a neural game simulator can be useful for downstream tasks like using it to train an agent with faster speed or empower the agent with a great forward model to help decision making.

### Questions
none

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper trains an action-conditional world model with diffusion for the environment of DOOM. The authors demonstrate that the model can be run in real-time at 20fps, and conduct ablations on the context length and necessity of noise augmentation during training to maintain stable generations.

### Strengths
Its fantastic that your model can run in real-time at 20+ fps. To me Section 3.3.2. is one of the most interesting parts of the paper. I would like to see this discussion expanded, and the important experiments/choices made moved from the appendix into the main paper. Especially since this is a substantial part of your contribution over other works.  

This paper also provides more evidence to the community that learning world models of complex environments is entirely feasible.

I very much like the direction of the paper, and feel that it is presented well. 
I do think this is good work that is of great interest to the community, but I cannot overlook the potential lack of novelty in relation to prior work given the current framing of the paper. Hence, the majority of my review is focussed on weaknesses.

### Weaknesses
# Major

## Prior work
The presentation of related/prior work is lacking in this paper.
There is substantial prior work in this domain which is either not mentioned or not correctly characterised.
In particular, "Diffusion for world modeling: Visual details matter in atari" cannot be considered concurrent work since it was first publicly available a year ago (in submission to last year's ICLR). Given the enormous similarities between your work and theirs, a much larger discussion is warranted - what is different/novel about your work compared to theirs, and more importantly highlight all of the similarities (being able to play in real-time, using diffusion for world modelling, architectural choices, etc). In addition, their paper utilises the model to train an RL agent, which makes progress towards addressing an important limitation you highlight about your work - "For example, our agent, even at the end of training, still does not explore all of the game’s locations and interactions, leading to erroneous behavior in those cases."

There is also no mention of GAIA-1, which simulates a complex real-world environment with a neural model.
Also no mention of "VideoGPT: Video Generation using VQ-VAE and Transformers" which also learns an action-conditional video prediction model for Doom.
"Temporally Consistent Transformers for Video Generation" also looks at long-term action conditional video generation quality. 

No mention of "Diffusion Forcing: Next-token Prediction Meets Full-Sequence Diffusion" that also uses the same noise augmentation during training to improve long term autoregressive generation. (Yes technically ICLR considers this contemporary work since it was first posted to arxiv on 1 July 2024)

# Minor

"...GameNGen extracts gameplay..." - what does this mean, are you making a claim about the representations learned? 

Figure 2 is unfair, the other papers were trained on very different data (notably without the HUD). At least try and use a comparable image when comparing your work to theirs. Given the higher resolution and increased visual fidelity of your model, there is no need to exaggerate the differences like this to highlight the improvements you've made.

Is there a need for a new definition of 'Interactive Environment' instead of using an existing formulation? Why doesn't a POMDP work, especially given your use of RL in the paper to generate the experiences.


### Questions
Why do you start with a pre-trained text-to-image diffusion model, what are the motivations for doing so? Is there not enough data to train from scratch?

Data wise, what kind of coverage do you have of the game? How does your model perform in areas where there is comparatively little data? "When playing with the model manually, we observe that some areas are very easy for both, some areas are very hard for both, and in some the agent performs much better" - suggests you have conducted some initial investigations into this, please elaborate more on this.

Can you clarify exactly how much data you train on, is it 70M transitions? How many epochs of training does this correspond to? ~90M sequences (batch size of 128 with ~700k training steps) are trained on of length 64, so each timestep is seen roughly 64 times?

For your context length experiments, do you have any qualitative results or observations on utilising longer context lengths? If an object is present say 50 frames in the past, would the 64 context length correctly remember this whereas the 32 frame one wouldn't? 

Given the open nature of the environment, will you be releasing code/data that could be used as a potential benchmark for future work in this area?

More discussion and examples on the long-term generations would be welcome (30 seconds/1 minute+). You mention that they are still hard to distinguish from real gameplay, but do they have a decent temporal consistency? Do the generations respect the geometry of the DOOM levels, do they always end up in specific areas, does the model count properly, etc.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors present a generative neural model which enables real-time controllable simulation of a complex game environment. This model is trained to reproduce Doom, using data gathered by training a separate RL agent in the VizDoom environment. They demonstrate that their model can produce high quality video output, and provide a variety of metrics to support this.

### Strengths
This is a clear, clean, well-presented paper, with impressive results. They have evaluated well, with interesting and relevant ablations and investigations. The chosen metrics seem well motivated and useful (LPIPS, PSNR, FVD). The desire for reproducibility is commendable and welcome, and I enjoyed the reverence they showed for Doom, having also “spent countless youth hours with the game”.

### Weaknesses
I think the paper’s biggest weakness lies in what the authors omit – I sense an understandable focus on what the model does _well_, and a glossing-over of what it might do _badly_. Some examples:

1. The human evaluation is run on clips of only 1.6 or 3.2 seconds. Why such short samples? Unless I missed it, no rationale is given for this, which leaves me to wonder whether the scores tail off significantly as the clips get longer.  
2.  (Minor) The claim in the abstract that the image reconstruction is comparable to “lossy JPEG compression” becomes less impressive when it’s revealed, in section 5.1, to correspond to a JPEG quality setting of only 20-30.  
3. Although it’s acknowledged (in 5.2.3) that certain map areas are “hard” or “easy”, there are no examples given of failure cases, or what it looks like when the model encounters a "hard" area.  
4. Section 5.2.1 acknowledges that context length is problematic (and this is discussed in section 7), but the negative consequences of this aren’t spelled out – again, I’d like to have seen failure cases due to the lack of context. It felt as though the supplementary material was slightly cherry-picked to avoid this.  


In the introduction, the authors posit the question _“Can a neural model running in real-time simulate a complex game at high quality?”_ and answer it with an unqualified “yes”. I recognise the impressive achievements in the paper, but this answer feels slightly dishonest – is the game genuinely playable (and enjoyable) in GameNGen, or are there still significant gaps to bridge? Can a level be played end-to-end? The PSNR scores are good, but they are not of themselves compelling evidence that the authors’ question can be answered in the affirmative. I think the paper would have been stronger if the answer to the posed question had been “Yes, _but_…”, or even “No, _but_…”

The second weakness in the paper is to do with _motivation_. Attempts to motivate the work by referring to a “new paradigm for game engines” feel a bit hand-wavy. Line 530 says that “the development process for video games under this new paradigm might be less costly and more accessible” – that’s a big “might”, when training GameNGen required 128 TPU-v5es, on top of training an RL agent to play the game in the first place. I find it hard to swallow any argument that a _new_ game can exist as weights of a neural model, rather than as lines of code: under the GameNGen paradigm, the game has to exist before the model can be trained. While the authors acknowledge that “many important questions remain”, I think it is possible to have a more grounded discussion around what these models can and can’t facilitate, and I would have liked to see this in the paper.

### Questions
Please consider these of lower priority – they are mainly for my own interest / to check my own understanding, and won’t necessarily have a bearing on my score.

1. I was very glad to see the ablations with the random agent, but it raised some questions:  
  a) Does it follow similar practices to the RL agent (eg biased towards repeating last action; using each action for four time steps, as per A.5)?  
  b) If not, could there be a significant distributional shift between the random actions and the human actions used for evaluation? Could this be compounding the low accuracy of the random model, alongside the problems caused by lack of exploration?  
  c) Given the difference in model performance between the random data and the trained data, did the authors consider _not_ including the initial random exploration from the trained agent in the dataset, but instead training (or evaluating) the agent for longer to get a higher quality dataset?

2. What was the benefit of adding noise at _different levels_ during training time? And how was the noise level chosen at inference time?

3. How long did the training take? 128 TPU-v5e devices for how long?

4. A question about the numbers – the paper states that the RL agent ran for a total of 50M environment steps, but lines 295-6 state that the generative model was trained on a “random subset of 70M examples”.

5. The section on human evaluation was not entirely clear. To check my understanding: a set of 130 pairs of clips was generated, starting from random locations – pairing the ground-truth with the model output, but only running the model for 64 (or 32) steps. On these pairs, the test subjects could identify the model’s output 58% or 60% of the time. Then a _second_ set of 150 clips was generated by rolling out the model for 6000 or 12000 steps (five or ten minutes), and then capturing the next 60 frames? In which case, what were users asked to compare these with? Around line 317 it’s mentioned that the predicted and ground-truth trajectories diverge after a few steps, so presumably after ten minutes they are significantly different. So is the human then presented with two very diverse clips, and asked to work out which is the prediction? This would surely make the comparison much harder, since they would not be comparing like for like. Would this explain why they only scored 50% in this test? Apologies if I've misunderstood the setup.

6. Is there a sense of what the pre-trained Stable Diffusion 1.4 brings to the table? Did the authors experiment with end-to-end training, or using different pre-trained text-to-image models?

7. Fig 13 – the plot indicates that the 70M dataset PSNR metric would keep going up if trained for longer – did the authors try going beyond 700K steps?

### Soundness
3

### Presentation
3

### Contribution
3
