require 'spec_helper'
require_relative '../factorial'

describe 'factorial' do
    it "gets factorial of 20" do
        factorial(20).should == 2432902008176640000
    end

    it "gets factorial of 0" do
        factorial(0).should == 1
    end

    it "gets factorial of 7" do
        factorial(7).should == 5040
    end
end