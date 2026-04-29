# Detection alone is insufficient to mitigate the harm by deepfake audio

- Decision: Reject
- Scores: 6, 7, 7

## Abstract
This paper confronts the challenge of detecting increasingly sophisticated deepfake audio from advanced Text-to-Speech (TTS) systems with voice cloning. We posit that achieving high-accuracy, long-term detection of synthetic audio, particularly against motivated adversaries, is likely an unrealistic goal. This stance is supported by two primary observations. Firstly, the ongoing advancements in TTS and Synthetic Speech Detection (SSD) mirror an offline Generative Adversarial Network dynamic, with TTS as the generator and SSD as the discriminator. This suggests an eventual convergence towards synthetic speech that is nearly indistinguishable from human speech, making detection inherently challenging, if not impossible, especially as SSD development inherently lags behind TTS progress because SSD relies on TTS to generate training data. Secondly, current SSDs demonstrate a critical vulnerability to active, malicious evasion attacks, where the audio is carefully edited to bypass the target SSDs. Consequently, addressing deepfake audio demands a more systematic and multifaceted strategy, integrating approaches such as detection, legislative frameworks, watermarking technologies, robust enforcement mechanisms, and fostering cultural awareness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper argues that relying solely on synthetic speech detection (SSD) to combat deepfake audio is a flawed and ultimately unsustainable strategy. The authors contend that TTS technology, which generates synthetic audio, is advancing at a rapid pace and is consistently outpacing SSD technology. This is because SSDs rely on data from new TTS systems to train their models, creating an inherent lag. As TTS systems produce increasingly human-like speech, the subtle artifacts that SSDs are trained to detect are minimized or eliminated, making detection more difficult.

The vulnerability of current SSDs to malicious adversarial attacks. The paper presents a systematic study demonstrating that SSDs can be evaded by deliberately perturbing the synthetic audio. These perturbations successfully deceive leading detection models, highlighting the fragility of current detection paradigms against determined attackers.

### Strengths
* Strong, Evidence-Based Argument: detection alone that is insufficient is well-supported by both a logical, theoretical framework (the TTS-SSD "arms race") and a concrete, experimental one (the adversarial attack study).
* Comprehensive Experimental Design: The study on adversarial attacks is a significant contribution. It systematically evaluates SSD vulnerabilities across different attack scenarios and on various datasets, providing concrete numbers and supporting data. The Attack Success Rate, VisQOL, and human ratings add credibility to the claim that the attacks are "stealthy."
* Actionable Recommendations: The conclusion moves beyond simply identifying the problem and offers a range of actionable recommendations for future research and policy, from proactive defense mechanisms like watermarking to ethical frameworks and legal recourse.

### Weaknesses
* Lack of Detail on Human Ratings: While Tables 5 and 6 summarize human ratings, the paper provides minimal information about the methodology. Details such as the number of raters, their background, etc., would be crucial for a thorough evaluation.
* Limited Discussion on Watermarking: The paper frequently suggests watermarking as a key part of the solution but provides very little detail on what this would entail.

### Questions
Why is the title different from the one submitted by the openreview system?

### Presentation
3

---

## Human Reviewer 2

### Rating
7

### Rating Number
7

### Confidence
3

### Summary
This paper argues that reliable detection of deepfake audio is likely unrealistic in the long term. It supports this through two main findings: 1) TTS systems are evolving faster than detection systems can keep up, and 2) current detection systems are vulnerable to malicious attacks that can bypass them while maintaining audio quality. The paper demonstrates these vulnerabilities through experiments with different attack methods and concludes that detection alone cannot be the solution to deepfake audio threats.

### Strengths
- Position is clear -- modern detection alone is insufficient for combating deepfake audio
- Critical security challenge as AI gets better and more pervasive
- Good coverage of literature in text to speech and synthetic speech detection
- Impressive set of experiments that demonstrate that modern detection systems are vulnerable to various attacks, especially for a motivated adversarial attacker
- Evaluation procedure considers human ratings

### Weaknesses
- The position is quite narrow given that the same problem translates to text and video as well. The paper can take a more expansive stance. 
- It is unclear if the detection still fails when multiple methods are used in an ensemble. 
- What if there is a confidence score attached to the prediction, and the reader can assess if they want to further examine the source based on the risk level? Binary yes/no is too blunt

### Questions
- Have you analyzed whether these attacks leave other detectable artifacts in the frequency domain or in other audio characteristics not currently used by detection systems?
- Given that your results suggest detection alone is insufficient, could you elaborate on how the proposed alternative solutions (watermarking, legislation, etc.) might interact with or complement detection approaches?
- The paper takes a strong stance that detection alone is insufficient, yet many other security domains (like spam detection or malware detection) continue to rely primarily on detection-based approaches. What makes deepfake audio fundamentally different from these other security challenges?

### Presentation
3

---

## Human Reviewer 3

### Rating
7

### Rating Number
7

### Confidence
3

### Summary
This paper advocates that achieving high-accuracy, long-term detection of synthetic audio is likely an unrealistic goal. This position is backed up by two observations. The first observation is that TTS and SSD are usually developing together, particularly SSD lags behind TTS due to relying on the newest TTS as training data. The second observation is that SSD is vulnerable to active attacks, meaning that the synthetic audio is deliberately edited to bypass the target SSDs; and the authors assessed the attack success rate to measure the effectiveness of the attacks under three scenarios: white-box, black-box, and agnostic.

### Strengths
This paper addresses a critical and rapidly evolving topic – the robustness of SSD amid the fast development in TTS technologies, which has significant societal implications. Specifically, it identifies two main issues: the rapid evolution of TTS outpacing SSD development, and the vulnerability of SSDs to deliberate adversarial perturbations. Additionally, it suggests possible solutions to these challenges.

The study systematically tests four SOTA SSD models across diverse attack scenarios (white-box, black-box and transfer-based agnostic attacks), combining objective metrics and human ratings. This systematic assessment strengthens the validity of findings.

Moreover, this paper also presents alternative views that emphasize ongoing research potential, maintaining a balanced view rather than one-sided pessimism.

### Weaknesses
While human ratings are included, the paper could elaborate on the methodology to strengthen claims about stealthiness, such as number of raters, their demographic backgrounds and the specific criteria used to assess similarity.

The paper briefly touches on future directions, such as legislative frameworks and watermarking technologies, but provides limited concrete suggestions. Expanding on these could enhance the discussion.

### Questions
1. Could you please elaborate on the human rating methodology? Specifically, how many raters were involved, and what were their backgrounds? This would help better assess the reliability of the stealthiness claims.

2. Given the demonstrated vulnerability of SSDs, do you have any idea for short-term promising solutions, before watermarking or legislative measures become widely adopted?

### Presentation
3
