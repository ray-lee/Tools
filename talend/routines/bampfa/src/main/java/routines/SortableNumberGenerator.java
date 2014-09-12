package routines;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Pattern;

import org.apache.commons.lang.StringUtils;

public class SortableNumberGenerator {
	private static final Pattern dotPattern = Pattern.compile("\\.");
	private static final Pattern isNumericPattern = Pattern.compile("^\\d+$");

	/**
	 * Computes a sortable object number for an object number.
	 *
	 * {talendTypes} String
	 *
	 * {Category} Sortable number generator
	 *
	 * {param} string("objectNumber") input: The BAM art object number.
	 *
	 * {example} computeSortableObjectNumber("2014.2.12") # 02014 00002 00012
	 */
	public static String computeSortableObjectNumber(String objectNumber) {
		String[] parts = dotPattern.split(objectNumber);
		List<String> sortableParts = new ArrayList<String>(parts.length);
		
		for (int i=0; i<parts.length; i++) {
			String part = parts[i];
			
			if (isNumericPattern.matcher(part).matches()) {
				part = StringUtils.leftPad(part, 5, '0');
			}
			else {
				part = part.toLowerCase();
			}
			
			sortableParts.add(part);
		}
		
		return StringUtils.join(sortableParts, " ");
	}
	
	public static void main(String[] args) {
		List<String> testObjectNumbers = Arrays.asList(
				"2014.1.12",
				"2014.123.4567",
				"1999.1.34.23.a",
				"TR.1.14.2");
		
		for (String objectNumber : testObjectNumbers) {
			System.out.println(objectNumber + ": " + computeSortableObjectNumber(objectNumber));
		}
	}
}
