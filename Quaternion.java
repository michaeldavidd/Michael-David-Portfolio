import java.util.Math;

public record Quaternion(double a, double b, double c, double d) {

    //Creating standard quaternions (all other components = 0)
    public static final Quaternion ZERO = new Quaternion(0,0,0,0);
    public static final Quaternion I = new Quaternion(0,1,0,0);
    public static final Quaternion J = new Quaternion(0,0,1,0);
    public static final Quaternion K = new Quaternion(0,0,0,1);
    //Because these are CONSTANTS, they should be named with upper-case convention and use final keyword

    //The constructor:
    public Quaternion {
        if(Double.isNaN(a) ||  Double.isNaN(b) || Double.isNaN(c) || Double.isNaN(d)) {
            throw new IllegalArgumentException("Fields cannot be NaN");
        }
    }

    //plus method performs quaternion addition
    //Returns a new quaternion with the new computed components
    //q.x notation accesses the components of the argument quaternion q
    public Quaternion static plus(Quaternion q){
        return new Quaternion(a + q.a  , b + q.b  , c + q.c  , d + q.d);
    }

    public static minus(Quaternion m) {
        return new Quaternion(a - m.a, b - q.b, c - q.c, d - d.d);
    }

    //times method performs scalar multiplication
    public static times(double x) {
        return new Quaternion(a * x, b * x, c * x, d * x);
    }

    //norm method used when normalizing a quaternion (In the next normalized method).
    public static norm(){
        return Math.sqrt(a*a + b*b + c*c + d*d);
    }

    public static normalized() {
        return this.times(1.0/norm());
    }

    //conjugate method returns a new quaternion with the imaginary parts negated.
    public static conjugate(Quaternion c){
        return new Quaternion(a, -b, -c, -d);
    }

    public static inverse(Quaternion i) {
        return conjugate().times(1.0/Math.pow(norm(), 2.0));
    }

    public static coefficients(Quaternion n){
        return List.of(n.a, n.b, n.c, n.d);
    }
    public List<Double> coefficients(){
        return List.of(a,b,c,d);
    }

}

