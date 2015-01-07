#!/usr/bin/python
""" Semantics of requirements and feature modelling domain

Feature Language
^^^^^^^^^^^^^^^^

The formal semantics are used to define the system's features. Features are 
specified using a combination of three phrases:

 * Action: The verb of the feature, what the feature is used to do.
 * Object: The subject of the feature, a noun-phrase describing the thing enabling the Action.
 * Result: The predicate of the feature, a noun-phrase describing the outcome of using the feature.

One illustrative (but facecious) example of a feature specified in this way 
is "delete the unfortunate frog on the virtual zoo page". In this example:

 * Action is *delete*
 * Object is *virtual zoo page*
 * Result is *unfortunate frog*

In plain English, this can be taken to mean that the system needs to have
some sort of virtual zoo page (whatever that is), where unfortunate frogs
(whatever they are) can be deleted (whatever that means). The meaning of
this feature would become clear if it was demonstrated by example (scenarios).

Note that Actions from one feature are never Results or Objects in another
feature. Every phrase used in the semantic feature langage is either a noun
or a verb (never both). Actions are always verbs, Objects and Results 
are always nouns. However, the Object of one feature may be the Result of
another feature, and vica-versa.


Scenario Language
^^^^^^^^^^^^^^^^^

Scenarios are basically stories about the feature being used.

Each scenario has a name that colloquially resembles the feature specification 
and also specifies who (which actor) is using the feature, plus potentially
some other distinguishing information about the particular instance of the
feature's use.

Scenarios also have a collection of sequential steps that are performed in
the scenario. This is the *meat and potatoes* of the scenario, a person
evaluating the system should be able to repeat those steps as they are 
described and get the expected result.

The most obvious scenarios describe what an actor **may do** with the system,
but there are also "Dissalowed" scenarios describing what a particular
actor **must not** be able to do with a particular system feature.

"""

class Catalogue: 
    _cat = []

    def fetch(self, name):
        for item in _cat:
            if item.name == name:
                return item
        raise Exception, 'item not found: %s' % name

    def fetch_all(self):
        return self._cat


## requirements model
class UCPCatalogue(Catalogue):
    _cat = []
    def register(self, name, description):
        for item in self._cat:
            if item.name == name:
                if item.description == description:
                    return item
                else:
                    msg = 'attempted redefinition of item %s (inconsistent descriptions)' % name
                    raise Exception, msg
        new = UseCasePackage(name, description)
        self._cat.append(new)
        return new

    def fetch_empty_packages(self):
        empty_pkgs = []
        for pkg in self.fetch_all():
            if len(pkg.use_cases()) == 0:
                empty_pkgs.append(pkg)
        return empty_pkgs

class UseCasePackage:
    _cat = UCPCatalogue()
    def __init__(self, name, description):
        self.name = name
        self.description = description
 
    def __repr__(self):
        return self.description

    def use_cases(self):
        """Return list of use-cases in this package"""
        ucs = []
        uc_cat = UCCatalogue()
        for uc in uc_cat._cat:
            if uc.package == self:
                if uc not in ucs:
                    ucs.append(uc)
        return ucs

    def __len__(self):
        return len(self.__repr__())

    @classmethod
    def register(self, name, description):
        return self._cat.register(name, description)

def ucp(name, description):
    return  UseCasePackage.register(name, description)


class UCCatalogue(Catalogue):
    _cat = []
    def __init__(self):  #, ucp_cat):
        #self._ucp_cat = ucp_cat
        pass

    def register(self, ucp, name, description):
        ucp_found = False
        for i in self._cat:
            if i.name == name and i.ucp == ucp:
                if item.description == description:
                    return item
                else:
                    msg = 'attempted redefinition of item %s (inconsistent descriptions)' % name
                    raise Exception, msg
        new = UseCase(ucp, name, description)
        self._cat.append(new)
        return new

    def featureless_ucs(self):
        featureless = []
        for uc in self.fetch_all():
            if len(uc.features()) == 0:
                featureless.append(uc)
        return featureless

class UseCase:
    _cat = UCCatalogue()
    def __init__(self, ucp, name, description):
        self.package = ucp
        self.name = name
        self.description = description
 
    def __repr__(self):
        return self.description

    def __len__(self):
        return len(self.__repr__())

    def features(self):
        fset = []
        for f in FeatureCatalogue().fetch_all():
            if f.use_case == self:
                fset.append(f)
        return fset

    def feature_specifications(self):
        specs = []
        for f in self.features():
            if f.specification not in specs:
                specs.append(f.specification)
        return specs

    def undefined_positive_scenarios(self):
        bads = []
        for feature in self.features():
            for scenario in feature.scenarios():
                if scenario.allowed and len(scenario.happy_story) == 0:
                    if scenario not in bads:
                        bads.append(scenario)
        return bads

    def undefined_negative_scenarios(self):
        bads = []
        for feature in self.features():
            for scenario in feature.scenarios():
                if not scenario.allowed and len(scenario.sad_story) == 0:
                    if scenario not in bads:
                        bads.append(scenario)
        return bads

    def undefined_scenarios(self):
        bads = self.undefined_positive_scenarios()
        for scenario in self.undefined_negative_scenarios():
            if scenario not in bads:
                bads.append(scenario)
        return bads
    
    def verbs_used(self):
        verbs = []
        for f in self.features():
            if f.specification.action not in verbs:
                verbs.append(f.specification.action)
        return verbs

    def nouns_used(self):
        nouns = []
        for f in self.features():
            obj = f.specification.obj
            result = f.specification.result
            if obj not in nouns:
                nouns.append(obj)
            if result not in nouns:
                nouns.append(result)
        return nouns

    @classmethod
    def register(self, ucp, name, description):
        return self._cat.register(ucp, name, description)

def use_case(ucp, name, description):
    return  UseCase.register(ucp, name, description)


class ActorCatalogue(Catalogue):
    _cat = []
    def register(self, name):
        for item in self._cat:
            if item.name == name:
                return item
        new = Actor(name)
        self._cat.append(new)
        return new

    def fetch_badly_described(self):
        badly_described = []
        for actor in self.fetch_all():
            if actor.description == None:
                badly_described.append(actor)
            if actor.description == actor.name and actor not in badly_described:
                badly_described.append(actor)
            if actor.description == '' and actor not in badly_described:
                badly_described.append(actor)
        return badly_described

    def fetch_unbound(self):
        unbound = []
        for actor in self.fetch_all():
            if len(actor.use_cases()) == 0:
                unbound.append(actor)
        return unbound

class Actor:
    _cat = ActorCatalogue()
    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def scenarios(self):
        my_scenarios = []
        for scenario in ScenarioCatalogue().fetch_all():
            if scenario.actor == self:
                my_scenarios.append(scenario)
        return my_scenarios

    def undefined_scenarios(self):
        undefineds = []
        for scenario in self.scenarios():
            if scenario.happy_story == [] and scenario.allowed:
                undefineds.append(scenario)
            elif not scenario.allowed and scenario.sad_story == []:
                undefineds.append(scenario)
        return undefineds

    def features(self):
        feat_list = []
        for feat in FeatureCatalogue().fetch_all():
            found=False
            for scenario in feat.scenarios():
                if scenario.actor == self:
                    found=True
            if found:
                feat_list.append(feat)
        return feat_list
    
    def use_cases(self):
        uc_list = []
        for feat in self.features():
            found = False
            for scenario in feat.scenarios():
                if scenario.actor == self:
                    found=True
            if found and feat.use_case not in uc_list:
                uc_list.append(feat.use_case)
        return uc_list

    def actions(self):
        """ list verbs of this actor's scenarios """
        actions = []
        for scenario in self.scenarios():
            act = scenario.feature.specification.action
            if act not in actions:
                actions.append(act)
        return actions

    def allowable_actions(self):
        allowable_actions = []
        for scenario in self.scenarios():
            if scenario.allowed:
                act = scenario.feature.specification.action
                if act not in allowable_actions:
                    allowable_actions.append(act)
        return allowable_actions

    def __repr__(self):
        return str(self.name)

    def __len__(self):
        return len(self.__repr__())
    
    @classmethod
    def register(self, name):
        return self._cat.register(name)

def actor(name, description=None):
    a = Actor.register(name)
    a.description = description
    return a

class PhraseCatalogue(Catalogue):
    def unused(self):
        bads = []
        for phrase in self.fetch_all():
            if len(phrase.features()) == 0 and phrase not in bads:
                bads.append(phrase)
        return bads
        

class VerbCatalogue(PhraseCatalogue):
    _cat = []
    def register(self, name, description):
        for item in self._cat:
            if item.name == name:
                if item.description == description:
                    return item
                else:
                    msg = 'attempted redefinition of item %s (inconsistent descriptions)' % name
                    raise Exception, msg
        new = Verb(name, description)
        self._cat.append(new)
        return new

class NounCatalogue(PhraseCatalogue):
    _cat = []
    def register(self, name, description):
        for item in self._cat:
            if item.name == name:
                if item.description == description:
                    return item
                else:
                    msg = 'attempted redefinition of item %s (inconsistent descriptions)' % name
                    raise Exception, msg
        new = Noun(name, description)
        self._cat.append(new)
        return new

class Phrase:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __repr__(self):
        return self.description

    def __len__(self):
        return len(self.__repr__())

    def code(self):
        #the_int = hash(self.name)
        #the_hex = hex(the_int)
        #return "code_%s" % the_hex
        import hashlib
        m = hashlib.md5()
        m.update(self.name)
        m.update(self.description)
        c = "code_%s" % m.hexdigest()
        return str(c)

    def scenarios(self, actor=None):
        scenarios = []
        for scenario in ScenarioCatalogue().fetch_all():
            spec = scenario.feature.specification
            found = False
            if spec.action == self:
                found = True
            if spec.result == self:
                found = True
            if spec.obj == self:
                found = True
            if found:
                if not actor or actor == scenario.actor:
                    scenarios.append(scenario)
        return scenarios

    def dissallowable_scenarios(self, actor):
        dissallowable_scenarios = []
        for s in self.scenarios(actor):
            if not s.allowed:
                dissallowable_scenarios.append(s)
        return dissallowable_scenarios
    
    def features(self, actor=None):
        features = []
        for feature in FeatureCatalogue().fetch_all():
            spec = feature.specification
            found = False
            if self in (spec.action, spec.result, spec.obj):
                if not actor or actor in feature.actors():
                    features.append(feature)
        return features

    def allowable_features(self, actor):
        allowable_features = []
        for f in self.features(actor):
            allowable = False
            for s in f.scenarios():
                if s.actor == actor and s.allowed:
                    allowable = True
            if allowable and f not in allowable_features:
                allowable_features.append(f)
        return allowable_features
                
    @classmethod
    def register(self, name, description):
        return self._cat.register(name, description)


class Verb(Phrase):
    _cat = VerbCatalogue()

    def results(self):
        nouns = []
        for f in self.features():
            result = f.specification.result
            if result not in nouns:
                nouns.append(result)
        return nouns

    def objects(self):
        nouns = []
        for f in self.features():
            obj = f.specification.obj
            if obj not in nouns:
                nouns.append(obj)
        return nouns

    def distinct_allowable_objs(self, actor):
        nouns = []
        for f in self.allowable_features(actor):
            if f.specification.obj not in nouns:
                nouns.append(f.specification.obj)
        return nouns
    
    def distinct_allowable_results(self, actor):
        nouns = []
        for f in self.allowable_features(actor):
            if  f.specification.result not in nouns:
                nouns.append(f.specification.result)
        return nouns

    def distinct_allowable_nouns(self, actor):
        nouns = self.distinct_allowable_objs(actor)
        for noun in self.distinct_allowable_results(actor):
            if noun not in nouns:
                nouns.append(noun)
        return nouns

    def distinct_allowable_binary_nouns(self, actor):
        nouns = []
        for f in self.allowable_features(actor):
            obj = f.specification.obj
            res = f.specification.result
            if obj == res and res not in nouns:
                nouns.append(res)
        return nouns

    def distinct_allowable_unidirectional_nouns(self, actor):
        nouns = []
        for f in self.allowable_features(actor):
            obj = f.specification.obj
            res = f.specification.result
            if obj != res:
                if res not in nouns:
                    nouns.append(res)
                if obj not in nouns:
                    nouns.append(obj)
        return nouns

    def distinct_dissallowable_scenario_objs(self, actor):
        nouns = []
        for s in self.dissallowable_scenarios(actor):
            n = s.feature.specification.obj
            if n not in nouns:
                nouns.append(n)
        return nouns

    def distinct_dissallowable_scenario_results(self, actor):
        nouns = []
        for s in self.dissallowable_scenarios(actor):
            n = s.feature.specification.result
            if n not in nouns:
                nouns.append(n)
        return nouns

    def distinct_dissallowable_scenario_nouns(self, actor):
        nouns = self.distinct_dissallowable_scenario_objs(actor)
        for n in self.distinct_disallowable_scenario_results(actor):
            if n not in nouns:
                nouns.append(n)
        return nouns

    def distinct_disallowable_scenario_binary_nouns(self, actor):
        nouns = []
        for s in self.disallowable_scenarios(actor):
            obj = s.feature.specification.obj
            res = s.feature.specification.result
            if obj == res and res not in nouns:
                nouns.append(res)
        return nouns
        
class Noun(Phrase):
    _cat = NounCatalogue()

    def result_of(self):
        verbs = []
        for f in self.features():
            verb = f.specification.action
            if f.specification.result == self and verb not in verbs:
                verbs.append(verb)
        return verbs
    
    def object_of(self):
        verbs = []
        for f in self.features():
            verb = f.specification.action
            if f.specification.obj == self and verb not in verbs:
                verbs.append(verb)
        return verbs
    

def verb(name, description):
    return  Verb.register(name, description)

def noun(name, description):
    return Noun.register(name, description)


class FeatureSpecificationCatalogue(Catalogue):
    _cat = []
    def register(self, action, result, obj):
        for i in self._cat:
            if i.action == action and i.result == result and i.obj == obj:
                return i
        new = FeatureSpecification(action, result, obj)
        self._cat.append(new)
        return new


class FeatureSpecification:
    _fs_cat = FeatureSpecificationCatalogue()

    def __init__(self, action, result, obj):
        self.action = action
        self.result = result
        self.obj = obj
    
    def __repr__(self):
        if self.result == self.obj:
            return "%s the %s" % (self.action, self.obj)
        msg = "%s the %s on the %s"
        return msg % (self.action, self.result, self.obj)

    @classmethod
    def register(self, action, result, obj):
        return self._fs_cat.register(action, result, obj)

def fspec(action, result, obj):
    return FeatureSpecification.register(action, result, obj)


class FeatureCatalogue(Catalogue):
    _cat = []
    def register(self, uc, fspec):
        for i in self._cat:
            if i.use_case == uc and i.specification == fspec:
                return i
        new = Feature(uc, fspec)
        self._cat.append(new)
        return new


class Feature:
    _cat = FeatureCatalogue()
    def __init__(self, uc, fspec):
        self.use_case = uc
        self.specification = fspec

    def scenarios(self, actor=None):
        sset = []
        for s in ScenarioCatalogue().fetch_all():
            if s.feature == self:
                if not actor or actor == s.actor:
                    sset.append(s)
        return sset

    def actors(self):
        """ list actors participating in scenarios of this feature """
        actor_list = []
        for scenario in self.scenarios():
            if scenario.actor not in actor_list:
                actor_list.append(scenario.actor)
        return actor_list

    def allowed_actors(self):
        actors = []
        for s in self.scenarios():
            if s.actor not in actors and s.allowed:
                actors.append(s.actor)
        return actors
    
    def __repr__(self):
        action = self.specification.action
        obj = self.specification.obj
        result = self.specification.result
        if result == obj:
            return "%s the %s" % (action, obj)
        msg = "%s the %s on the %s"
        return msg % (action, result, obj)

    def __len__(self):
        return len(self.__repr__())
    
    @classmethod
    def register(self, uc, fspec):
        return self._cat.register(uc, fspec)

def feature(uc, action, result, obj):
    fspec = FeatureSpecification.register(action, result, obj)
    return Feature.register(uc, fspec)


class ScenarioCatalogue(Catalogue):
    _cat = []
    def register(self, feat, actor, name, allowed=True):
        for i in self._cat:
            if i.feature == feat and i.actor == actor and i.name == name:
                if allowed == i.allowed:
                    return i
                else:
                    msg =  "contracitcionary permissions defined for %s on %s" % (actor, feat)
                    raise Exception, msg
        new = Scenario(feat, actor, name, allowed)
        self._cat.append(new)
        return new

    def siblings(self, scenario):
        sibs = []
        for s in self._cat:
            if s != scenario:
                if s.feature == scenario.feature and s.name == scenario.name:
                    sibs.append(s)
        return sibs

    
    def generate(self):
        for s in self._cat:
            actorsuper = [(s.actor, s.allowed),] + s.alternate_actors
            for (actor, allowed) in actorsuper:
                fixsuper = [s.fixtures,]
                if len(s.alternate_fixtures) > 0:
                    for altfix in s.alternate_fixtures:
                        fsuper.append(altrix)
                
                for fset in fixsuper:
                    inferred = self.register(s.feature, actor, s.name, allowed)
                    for fix in fset:
                        inferred.fixture(fix)
                    if inferred.happy_story == []:
                        inferred.happy_story = s.happy_story
                    if inferred.sad_story == []:
                        inferred.sad_story = s.sad_story



class Scenario:
    _cat = ScenarioCatalogue()

    def __init__(self, feat, actor, name, allowed=True):
        self.name = name
        self.feature = feat
        self.actor = actor
        self.allowed = allowed
        self.alternate_actors = []
        self.fixtures = []
        self.alternate_fixtures = []
        self.happy_story = []
        self.sad_story = []

    def alternate_actor(self, actor, allowed=True):
        if actor not in self.alternate_actors:
            self.alternate_actors.append((actor, allowed))

    def fixture(self,fix):
        if fix not in self.fixtures:
            self.fixtures.append(fix)

    def alternate_fixture_set(self, fix_set):
        if fix_set not in self.alternate_fixtures:
            self.alternate_fixtures.append(fix_set)

    def _story(self, sentence):
        self.happy_story.append(sentence)

    def given(self, sentence):
        self._story("Given %s" % sentence)

    def and_(self, sentence):
        self._story("And %s" % sentence)

    def then(self, sentence):
        self._story("Then %s" % sentence)

    def _sad_story(self, sentence):
        self.sad_story.append(sentence)

    def sad_given(self, sentence):
        self._sad_story("Given %s" % sentence)
        
    def sad_and(self, sentence):
        self._sad_story("And %s" % sentence)
        
    def sad_then(self, sentence):
        self._sad_story("Then %s" % sentence)

    def __repr__(self):
        return "(%s) %s" % (self.actor, self.name)

    def __len__(self):
        return len(self.__repr__())
    
    @classmethod
    def register(self, feat, actor, name, allowed=True):
        return self._cat.register(feat, actor, name, allowed)


def scenario(uc, action, result, obj, name, actor, allowed=True):
    f = feature(uc, action, result, obj)
    return Scenario.register(f, actor, name, allowed)


# TODO: wrap remaining classes in function, classmethod, catalogue pattern
# create CLI program
# test ontology classes
# implement jinja templates to generate rst (from CLI program)
# incorporate into Makefile (doc buildout, testing)


def runapp():
    from optparse import OptionParser
    from jinja2 import Environment, PackageLoader

    env = Environment(loader=PackageLoader('dsl', 'templates'))

    parser = OptionParser("behavior.py [options]")

    parser.add_option(
        "--gerkin",
        dest='gerkin',
        action='store_true',
        help='Generate feature specifications (gerkin language) for BDD testing framework')
    parser.add_option(
        "--rst",
        dest="rst", #action="store_true",
        help='Generate restructured text format documentation (for Sphinx doc generator)')
    parser.add_option("--foo", dest="foo", action="store_true",
                      help="dummy action for debugging etc")

    (opts, args) = parser.parse_args()

    print "generating..."
    ScenarioCatalogue().generate()

    if opts.gerkin:
        raise Exception, "not implemented yet"

    if opts.rst:
        packages = UCPCatalogue().fetch_all()
        actors = ActorCatalogue().fetch_all()
        nouns = NounCatalogue().fetch_all()
        verbs = VerbCatalogue().fetch_all()

        # index.rst (document root) is hardcoded
        # chapter 1 is hardcoded, see introduction.rst
        # chapter 2: (Analysis) generated
        # TODO
        
        # chapter 3: (Requirements) generated   
        req_template = env.get_template('requirements.rst.tmpl')
        req_file = open('%s/requirements.rst' % opts.rst, 'w+')
        req_file.write(
            req_template.render(
                packages=packages,
                actors=actors))
        req_file.close()

        # feature docs no longer include scenarios directly,
        # but they still contain links.
        feature_template = env.get_template('feature.rst.tmpl')
        for ucp in packages:
            for uc in ucp.use_cases():
                for f in uc.features():
                    fname = '%s/features/%s.rst' % (opts.rst, str(f).replace(' ', '_'))
                    feature_file = open(fname, 'w+')
                    feature_file.write(
                        feature_template.render(feature=f))
                    feature_file.close()

        lettuce_template = env.get_template('lettuce.txt.tmpl')
        for ucp in packages:
            for uc in ucp.use_cases():
                for f in uc.features():
                    a = str(f.specification.action.name).replace(' ','_')
                    r = str(f.specification.result.name).replace(' ','_')
                    o = str(f.specification.obj.name).replace(' ','_')
                    fstr = '%s__%s__%s' % (a, r, o)
                    uc_str = str(uc).replace('/','-').replace(' ','_')
                    fname = '%s/../features/generated_%s_%s.feature' % (opts.rst, uc_str, fstr)
                    lettuce_file = open(fname, 'w+')
                    lettuce_file.write(
                        lettuce_template.render(feature=f))
                    lettuce_file.close()

        # chapter 4: (Actors) generated
        actor_template = env.get_template('actors.rst.tmpl')
        fname = '%s/actors.rst' % (opts.rst,)
        actor_file = open(fname, 'w+')
        actor_file.write(actor_template.render(actors=actors))
        actor_file.close()

        # chapter 5: (Glossary) generated
        req_template = env.get_template('glossary.rst.tmpl')
        req_file = open('%s/glossary.rst' % opts.rst, 'w+')
        req_file.write(
            req_template.render(nouns=nouns, verbs=verbs))
        req_file.close()

        # chapter 6: (Testing/Accpetance)
        tmpl = env.get_template('testing.rst.tmpl')
        fname = '%s/testing.rst' % opts.rst
        fp = open(fname, 'w+')
        fp.write(
            tmpl.render(
                sc=ScenarioCatalogue(),
                ac=ActorCatalogue(), ))
        fp.close()

        # chapter 7: (ongoing analysis)
        tmpl = env.get_template('analysis.rst.tmpl')
        fname = '%s/analysis.rst' % opts.rst
        fp = open(fname, 'w+')
        fp.write(
            tmpl.render(
                ac=ActorCatalogue(),
                ucpc=UCPCatalogue(),
                ucc=UCCatalogue(),
                vc = VerbCatalogue(),
                nc = NounCatalogue(), ))
        fp.close()
