# This software is distributed under the 3-clause BSD License.
import mpisppy.cylinders.spoke

class FrankWolfeOuterBound(mpisppy.cylinders.spoke.OuterBoundSpoke):

    converger_spoke_char = 'F'

    def main(self):
        self.opt.fwph_main()

    def is_converged(self):
        return self.got_kill_signal()

    def sync(self):
        # Tell the hub about the most recent bound
        self.bound = self.opt._local_bound

    def finalize(self):
        self.bound = self.opt._local_bound
        self.final_bound = self.opt._local_bound
        return self.final_bound
