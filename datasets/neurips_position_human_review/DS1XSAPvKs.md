# Position: Machine Learning Conferences Should Establish a "Refutations and Critiques" Track

- Decision: Accept (Oral)
- Scores: 8, 7, 6

## Abstract
Science progresses by iteratively advancing and correcting humanity's understanding of the world. In machine learning (ML) research, rapid advancements have led to an explosion of publications, but have also led to misleading, incorrect, flawed or perhaps even fraudulent studies being accepted and sometimes highlighted at ML conferences due to the fallibility of peer review. While such mistakes are understandable, ML conferences do not offer robust processes to help the field systematically correct when such errors are made.
This position paper argues that ML conferences should establish a dedicated "Refutations and Critiques" (R&C) Track. This R&C Track would provide a high-profile, reputable platform to support vital research that critically challenges prior research, thereby fostering a dynamic self-correcting research ecosystem.
We discuss key considerations including track design, review principles, potential pitfalls, and provide an illustrative example submission concerning a recent ICLR 2025 Oral.
We conclude that ML conferences should create official, reputable mechanisms to help ML research self-correct.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This position paper argues that major machine learning conferences should establish a dedicated "Responses and Critiques" (R&C) Track to provide an official, reputable platform for critically challenging prior research. The authors contend that the current peer review process is fallible, leading to the acceptance of misleading or flawed research. They highlight the lack of official mechanisms for rectifying the scientific record once such papers are published, which forces researchers to use suboptimal, informal channels like social media to voice concerns. The paper supports this position with multiple examples of highly-cited papers that have been publicly contested for various reasons, including flawed methodology, un-reproducible results, or lack of novelty. The authors propose that an R&C track, similar to the NeurIPS Datasets and Benchmarks track, would formalize this corrective process and help the field self-correct, ultimately improving the integrity and reliability of ML research.

### Strengths
The paper presents a very clear and compelling argument for a "Responses and Critiques" track at machine learning conferences. The authors effectively support their position by providing numerous specific examples of high-profile papers that have been contested by the community, demonstrating a clear problem with the current system. The paper's argument is well-reasoned, highlighting the shortcomings of the existing peer review process and the negative consequences of relying on informal channels for scientific critique. The proposal is well-developed, with considerations for naming, review principles, and potential pitfalls. The analogy to the NeurIPS Datasets and Benchmarks track is a particularly strong point, as it provides a precedent for creating a new track to address a systemic issue. The illustrative example of a potential R&C submission is a very effective way to show what the authors envision for the track.

### Weaknesses
The paper is quite strong, and the weaknesses are minor. The primary area for improvement would be to more explicitly address the potential for an R&C track to be abused. While the authors touch on potential pitfalls, a more detailed discussion of how to prevent a track from being used for personal attacks, retaliatory reviews, or to target specific authors would strengthen the argument. The paper does not explicitly consider how the proposed track would interact with and be overseen by conference committees to prevent such misuse.

### Questions
* How would you propose to handle the submission and review process to prevent the R&C track from becoming a venue for personal attacks or retaliatory submissions?
* You mention that the R&C track could be a pilot program. What specific metrics would you use to evaluate its success and determine if it should be continued or expanded?

### Presentation
3

---

## Human Reviewer 2

### Rating
7

### Rating Number
7

### Confidence
5

### Summary
In this paper, the authors argue that major ML conferences need a dedicated “Responses & Critiques” (R&C) track to streamline and formalize post-publication review and correction. They argue with supporting evidence that the peer review process is not infallible and can suffer from false positives where flawed or overstated papers may be accepted for publication. The paper discusses the current, arguably slow and unorganized alternatives of errata, blogs, reproducibility challenges, etc. As an alternative, it proposes a juried R&C track within the conference timeline (with proceedings) where already-published conference papers will be submitted and judged on four criteria -- rigor, substance, constructiveness, and significance. To this end, reviewer guidelines have been given along with an outline of author-response rights. To demonstrate the feasibility, an exemplary 20-page mock critique of a recent ICLR paper
has been given. Potential downside of reviewer burden, the risk of hostile critiques, and moderation logistics have been discussed. The authors appeal that such detailed critiques should be treated as proper research contributions and made official.

### Strengths
The core arguments of the paper are very clear, well-structured, and concise, which makes the paper easy to follow. It provides strong supporting evidence (Sec 2.1) that several papers published in top-tier venues (eg, "*Privacy for Free: How does Dataset Condensation Help Privacy?*", "*Learning to Summarize from Human Feedback*", etc.) are either overstated or lack novelty or misguiding claims. The four criteria of the proposed R&C track are clearly stated in Sec 3.5. It also discusses alternative solutions adequately, such as the Reproducibility Challenge, negative results venues, and stricter checklists (Sec 4).  The 20-page mock critique of a recent ICLR paper serves as an effective proof-of-concept.

### Weaknesses
Although the paper has significant merits, I feel certain issues can be resolved to strengthen it:

**More quantitative evidence**: A clear statistics of how many NeurIPS best-paper nominees were later disputed or how citation‐decay differs once a critique appears will be helpful. 

**Pilot Specifications**: In Sec 3, the authors mention a pilot. However, I do not see any estimates of expected submissions, reviewer hours, or the pre-review screening thresholds. Adding those projections would make the feasibility argument stronger. 

**Risk Mitigation**: Although the risks of “*frivolous, adversarial*” possibilities are discussed (Sec 4), no execution plan is outlined. Also, details related to screening stages and conflict-of-interest management are missing. 

**Additional comparisons**: Certain important alternatives, such as overlay journals (that include peer-reviewed discussion threads to arXiv posts), OpenReview comments, ICML public-comment threads, and code-audit tracks, have not been compared in the same light as reproducibility challenges and negative-result journals.

**Typos**: Line 209 -- should it be “Responses and Critiques" instead of "Refutations and Corrections"?

### Questions
I am wondering how one can measure the success of the pilot track. Would love to understand that.

### Presentation
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
This position paper proposes the establishment of a dedicated “Responses and Critiques” (R&C) track at Machine Learning (ML) conferences. It begins by reviewing existing problems in the field to demonstrate the need for such a track. The paper then outlines a possible track design, discussing its name, the rationale for its separation from the main conference, and its guiding principles. Finally, it considers alternatives and contrasts the proposed track with existing approaches.

### Strengths
* The idea of having an R&C track as a generalization of reporducibility is sound.
* The discussion on existing pitfalls is thorough and complete.

### Weaknesses
* The paper's thorough analysis of existing pitfalls is not matched by an equally rigorous design for the proposed R&C track. In comparison to the detailed critique of current pitfalls, the proposed solution appears less thorough and somewhat handwaving.
* The proposal overlooks the critical operational detail of the review timeline (see question). In particular, there is less discussion on leveraging the longer, more rigorous review process of academic journals to ensure the quality of the track. This possibility is only addressed only in a fragmented and cursory manner.
* To prevent adversarial submissions, the authors rely heavily on the guiding principles from Section 3.5. While commendable, these principles seem idealistic. The paper would be more persuasive if it also proposed concrete mechanisms and actionable steps to ensure the track's successful launch.

### Questions
The paper rightly argues that the compressed timeline of ML conferences undermines the rigor of the review process, as discussed in Section 2.1 and 2.3. However, this same logic seems to create a challenge for the proposed R&C track itself. If the R&C track must also adhere to a standard conference schedule, it's hard to see how it could avoid the same pitfalls. The proposal's goal (Section 4) of enabling "multiple rounds of author-reviewer interaction" seems fundamentally impossible with a fast-paced timeline, which raises the concern that the R&C papers themselves could be rushed and flawed. I'd love to hear the authors' opinions on this---should the R&C track be of a different timeline? If so, would a journal (say, TMLR) followed by a journal-to-conference presentation a better solution?

Another idealistic design that I have a question on is for "authors of critiqued papers to provide responses." Are authors required to do so? If so, would it create a possibility for hominem attackers to DoS the authors?

### Presentation
3
