import requests
import xml.etree.ElementTree as ET
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment

def fetch_sitemap_urls(sitemap_url):
    """Fetch and parse sitemap XML to extract URLs."""
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()
        
        # Parse XML
        root = ET.fromstring(response.content)
        
        # Extract URLs from sitemap
        # Sitemaps use the namespace http://www.sitemaps.org/schemas/sitemap/0.9
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = []
        
        for url in root.findall('ns:url', namespace):
            loc = url.find('ns:loc', namespace)
            if loc is not None:
                urls.append(loc.text)
        
        return urls
    except Exception as e:
        print(f"Error fetching {sitemap_url}: {e}")
        return []

def save_to_excel(all_urls, filename='sitemap_urls.xlsx'):
    """Save URLs to Excel file."""
    # Create workbook and select active sheet
    wb = Workbook()
    ws = wb.active
    ws.title = "Sitemap URLs"
    
    # Add header
    ws['A1'] = 'No.'
    ws['B1'] = 'URL'
    ws['C1'] = 'Source Sitemap'
    
    # Style header
    for cell in ['A1', 'B1', 'C1']:
        ws[cell].font = Font(bold=True)
        ws[cell].alignment = Alignment(horizontal='center')
    
    # Add URLs
    row = 2
    for url_data in all_urls:
        ws[f'A{row}'] = row - 1
        ws[f'B{row}'] = url_data['url']
        ws[f'C{row}'] = url_data['source']
        row += 1
    
    # Adjust column widths
    ws.column_dimensions['A'].width = 8
    ws.column_dimensions['B'].width = 80
    ws.column_dimensions['C'].width = 40
    
    # Save workbook
    wb.save(filename)
    print(f"\n✓ Successfully saved {row-2} URLs to {filename}")

def main():
    # Sitemap URLs
    sitemaps = [
        'https://legalwritingexperts.com/sitemap-posts-1.xml',
        'https://legalwritingexperts.com/sitemap-posts-2.xml'
    ]
    
    all_urls = []
    
    print("Fetching URLs from sitemaps...\n")
    
    # Fetch URLs from each sitemap
    for sitemap_url in sitemaps:
        print(f"Processing: {sitemap_url}")
        urls = fetch_sitemap_urls(sitemap_url)
        print(f"  Found {len(urls)} URLs")
        
        # Add to collection with source information
        for url in urls:
            all_urls.append({
                'url': url,
                'source': sitemap_url
            })
    
    # Save to Excel
    if all_urls:
        save_to_excel(all_urls)
        print(f"\nTotal URLs collected: {len(all_urls)}")
    else:
        print("\nNo URLs found!")

if __name__ == "__main__":
    main()
